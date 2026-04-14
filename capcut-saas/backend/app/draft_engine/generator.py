"""
Draft Generator - Core module for generating CapCut drafts from templates

This module integrates with pyJianYingDraft to generate draft_content.json files.
"""
from typing import Dict, Any, Optional
import json

from pyJianYingDraft import ScriptFile, DraftFolder, TrackType, VideoSegment, AudioSegment, TextSegment, trange, tim


class DraftGenerator:
    """Generates CapCut drafts from templates and user materials"""

    def __init__(self):
        pass

    def generate(
        self,
        template_content: Dict[str, Any],
        materials_mapping: Dict[str, Dict[str, Any]],
        text_replacements: Dict[str, str],
        output_settings: Dict[str, Any],
    ) -> Dict[str, Any]:
        """
        Generate a draft based on template and material mappings.

        Args:
            template_content: The parsed template JSON (draft_content.json)
            materials_mapping: Map of template material names to material info dicts
                {
                    "template_material_name": {
                        "id": "material_uuid",
                        "path": "storage_path",
                        "type": "video/audio/image",
                        "filename": "file.mp4"
                    }
                }
            text_replacements: Map of segment IDs to replacement text
            output_settings: {width, height, fps}

        Returns:
            Generated draft_content.json as dict
        """
        # Load template using pyJianYingDraft's template mode
        script = ScriptFile.load_template_from_dict(template_content)

        # Apply material replacements
        self._replace_materials(script, materials_mapping)

        # Apply text replacements
        self._replace_text(script, text_replacements)

        # Apply output settings
        if output_settings:
            if "width" in output_settings:
                script.width = output_settings["width"]
            if "height" in output_settings:
                script.height = output_settings["height"]
            if "fps" in output_settings:
                script.fps = output_settings["fps"]

        # Export to JSON
        return script.dumps()

    def _replace_materials(
        self,
        script: ScriptFile,
        materials_mapping: Dict[str, Dict[str, Any]],
    ):
        """Replace template materials with actual uploaded materials"""
        for template_name, material_info in materials_mapping.items():
            # In template mode, we use replace_material_by_name
            # The material_id in the template maps to our material storage path
            try:
                script.replace_material_by_name(template_name, material_info["path"])
            except Exception as e:
                print(f"Warning: Could not replace material {template_name}: {e}")

    def _replace_text(
        self,
        script: ScriptFile,
        text_replacements: Dict[str, str],
    ):
        """Replace text content in template"""
        for segment_id, new_text in text_replacements.items():
            try:
                script.replace_text(segment_id, new_text)
            except Exception as e:
                print(f"Warning: Could not replace text {segment_id}: {e}")

    def generate_from_scratch(
        self,
        project_name: str,
        tracks_config: list[Dict[str, Any]],
        output_settings: Dict[str, Any],
    ) -> ScriptFile:
        """
        Create a draft from scratch with specified track configuration.

        Args:
            project_name: Name of the project
            tracks_config: List of track configurations
                [
                    {
                        "type": "video",
                        "segments": [
                            {
                                "material_path": "path/to/video.mp4",
                                "timerange": {"start": "0s", "duration": "5s"},
                                "speed": 1.0,
                                "volume": 0.8
                            }
                        ]
                    },
                    {"type": "audio", "segments": [...]},
                    {"type": "text", "segments": [...]}
                ]
            output_settings: {width, height, fps}

        Returns:
            ScriptFile instance
        """
        script = ScriptFile(
            width=output_settings.get("width", 1920),
            height=output_settings.get("height", 1080),
            fps=output_settings.get("fps", 30),
            maintrack_adsorb=True,
        )

        for track_config in tracks_config:
            track_type_str = track_config.get("type", "video")
            try:
                track_type = TrackType[track_type_str]
            except KeyError:
                print(f"Warning: Unknown track type {track_type_str}, skipping")
                continue

            track_name = track_config.get("name", track_type.name)
            script.add_track(track_type, track_name)

            for seg_config in track_config.get("segments", []):
                segment = self._create_segment(track_type, seg_config)
                if segment:
                    script.add_segment(segment, track_name)

        return script

    def _create_segment(
        self,
        track_type: TrackType,
        seg_config: Dict[str, Any],
    ):
        """Create a segment based on track type and config"""
        material_path = seg_config.get("material_path")
        timerange = seg_config.get("timerange", {"start": "0s", "duration": "5s"})
        start = timerange.get("start", "0s")
        duration = timerange.get("duration", "5s")

        try:
            if track_type == TrackType.video:
                return VideoSegment(
                    material_path,
                    trange(start, duration),
                    speed=seg_config.get("speed", 1.0),
                    volume=seg_config.get("volume", 1.0),
                )
            elif track_type == TrackType.audio:
                return AudioSegment(
                    material_path,
                    trange(start, duration),
                    speed=seg_config.get("speed", 1.0),
                    volume=seg_config.get("volume", 1.0),
                )
            elif track_type == TrackType.text:
                return TextSegment(
                    seg_config.get("text", ""),
                    trange(start, duration),
                )
        except Exception as e:
            print(f"Warning: Could not create segment: {e}")
            return None
