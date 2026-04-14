import React, { useState, useEffect } from 'react'
import { Card, Form, Select, Button, message, Steps, Result, Spin } from 'antd'
import { useLocation, useNavigate } from 'react-router-dom'
import { api } from '../services/api'

interface Template {
  id: string
  name: string
  description?: string
  metadata?: any
}

interface Material {
  id: string
  type: string
  filename: string
}

const DraftGenerator: React.FC = () => {
  const [templates, setTemplates] = useState<Template[]>([])
  const [materials, setMaterials] = useState<Material[]>([])
  const [selectedTemplate, setSelectedTemplate] = useState<string | null>(null)
  const [selectedMaterials, setSelectedMaterials] = useState<Record<string, string>>({})
  const [loading, setLoading] = useState(false)
  const [currentStep, setCurrentStep] = useState(0)
  const [generatedDraftId, setGeneratedDraftId] = useState<string | null>(null)
  const [form] = Form.useForm()
  const location = useLocation()
  const [workspaceId] = useState<string>('default')
  const projectId = location.state?.projectId || 'default'

  useEffect(() => {
    loadData()
  }, [])

  const loadData = async () => {
    try {
      const [templatesRes, materialsRes] = await Promise.all([
        api.getTemplates(workspaceId),
        api.getMaterials(workspaceId),
      ])
      setTemplates(templatesRes.data)
      setMaterials(materialsRes.data)
    } catch (error) {
      message.error('Failed to load data')
    }
  }

  const handleGenerate = async () => {
    if (!selectedTemplate) {
      message.error('Please select a template')
      return
    }

    setLoading(true)
    try {
      const response = await api.generateDraft(workspaceId, projectId, {
        template_id: selectedTemplate,
        materials_mapping: selectedMaterials,
        text_replacements: {},
        options: {},
      })
      setGeneratedDraftId(response.data.id)
      setCurrentStep(2)
      message.success('Draft generated successfully!')
    } catch (error) {
      message.error('Failed to generate draft')
    } finally {
      setLoading(false)
    }
  }

  const handleExport = async () => {
    if (!generatedDraftId) return

    try {
      const response = await api.exportDraft(workspaceId, projectId, generatedDraftId)
      // Create downloadable JSON file
      const blob = new Blob([JSON.stringify(response.data, null, 2)], { type: 'application/json' })
      const url = URL.createObjectURL(blob)
      const a = document.createElement('a')
      a.href = url
      a.download = 'draft_content.json'
      a.click()
      URL.revokeObjectURL(url)
      message.success('Draft exported!')
    } catch (error) {
      message.error('Failed to export draft')
    }
  }

  const templateMaterials = selectedTemplate
    ? templates.find((t) => t.id === selectedTemplate)?.metadata?.material_names || []
    : []

  return (
    <div>
      <h1>Generate Draft</h1>

      <Steps current={currentStep} items={[{ title: 'Select Template' }, { title: 'Map Materials' }, { title: 'Generate' }]} />

      <Card style={{ marginTop: 24 }}>
        {currentStep === 0 && (
          <Form form={form} layout="vertical">
            <Form.Item label="Select Template" required>
              <Select
                placeholder="Choose a template"
                value={selectedTemplate}
                onChange={(value) => {
                  setSelectedTemplate(value)
                  setSelectedMaterials({})
                }}
                options={templates.map((t) => ({ value: t.id, label: t.name }))}
              />
            </Form.Item>
            <Button type="primary" onClick={() => setCurrentStep(1)} disabled={!selectedTemplate}>
              Next
            </Button>
          </Form>
        )}

        {currentStep === 1 && (
          <Form layout="vertical">
            <Form.Item label="Map Materials">
              {templateMaterials.map((materialName: string) => (
                <Form.Item key={materialName} label={materialName} required>
                  <Select
                    placeholder={`Select ${materialName}`}
                    onChange={(value) => setSelectedMaterials({ ...selectedMaterials, [materialName]: value })}
                    options={materials.map((m) => ({ value: m.id, label: `${m.filename} (${m.type})` }))}
                  />
                </Form.Item>
              ))}
            </Form.Item>
            <Button onClick={() => setCurrentStep(0)}>Back</Button>
            <Button type="primary" onClick={handleGenerate} loading={loading} style={{ marginLeft: 8 }}>
              Generate Draft
            </Button>
          </Form>
        )}

        {currentStep === 2 && (
          <Result
            status="success"
            title="Draft Generated Successfully!"
            subTitle="Download the draft JSON file and import it into CapCut."
            extra={[
              <Button type="primary" key="export" onClick={handleExport}>
                Download Draft JSON
              </Button>,
              <Button key="another" onClick={() => setCurrentStep(0)}>
                Generate Another
              </Button>,
            ]}
          />
        )}
      </Card>
    </div>
  )
}

export default DraftGenerator
