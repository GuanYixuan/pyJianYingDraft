import React, { useState, useEffect } from 'react'
import { Table, Tag, Space, Button, message, Card, Select, Modal, Descriptions, Spin } from 'antd'
import { PlayCircleOutlined, DownloadOutlined, DeleteOutlined } from '@ant-design/icons'
import { api } from '../services/api'

const { Option } = Select

interface FinalVideo {
  id: string
  order_id: string
  user_id: string
  workspace_id: string
  filename: string
  storage_path: string
  duration_ms: number | null
  thumbnail_url: string | null
  file_size_bytes: number | null
  source_draft_id: string | null
  publish_status: {
    douyin: { published: boolean }
    wechat_channels: { published: boolean }
  }
  created_at: string
}

interface Workspace {
  id: string
  name: string
  role: string
}

const FinalVideos: React.FC = () => {
  const [videos, setVideos] = useState<FinalVideo[]>([])
  const [workspaces, setWorkspaces] = useState<Workspace[]>([])
  const [selectedWorkspace, setSelectedWorkspace] = useState<string | null>(null)
  const [loading, setLoading] = useState(false)
  const [detailModalVisible, setDetailModalVisible] = useState(false)
  const [selectedVideo, setSelectedVideo] = useState<FinalVideo | null>(null)
  const [videoDetail, setVideoDetail] = useState<any>(null)
  const [detailLoading, setDetailLoading] = useState(false)

  useEffect(() => {
    fetchWorkspaces()
  }, [])

  useEffect(() => {
    if (selectedWorkspace) {
      fetchVideos(selectedWorkspace)
    }
  }, [selectedWorkspace])

  const fetchWorkspaces = async () => {
    try {
      const response = await api.getWorkspaces()
      setWorkspaces(response.data)
      if (response.data.length > 0 && !selectedWorkspace) {
        setSelectedWorkspace(response.data[0].id)
      }
    } catch (error) {
      message.error('Failed to fetch workspaces')
    }
  }

  const fetchVideos = async (workspaceId: string) => {
    setLoading(true)
    try {
      const response = await api.getFinalVideos(workspaceId)
      setVideos(response.data)
    } catch (error) {
      message.error('Failed to fetch videos')
    } finally {
      setLoading(false)
    }
  }

  const handleDownload = async (video: FinalVideo) => {
    try {
      const response = await api.getFinalVideoDownloadUrl(video.id)
      window.open(response.data.download_url, '_blank')
    } catch (error) {
      message.error('Failed to get download URL')
    }
  }

  const handleDelete = async (video: FinalVideo) => {
    Modal.confirm({
      title: 'Delete Video',
      content: 'Are you sure you want to delete this video?',
      onOk: async () => {
        try {
          await api.deleteFinalVideo(video.id)
          message.success('Video deleted successfully')
          if (selectedWorkspace) {
            fetchVideos(selectedWorkspace)
          }
        } catch (error: any) {
          message.error(error.response?.data?.detail || 'Failed to delete video')
        }
      },
    })
  }

  const handleViewDetail = async (video: FinalVideo) => {
    setSelectedVideo(video)
    setDetailModalVisible(true)
    setDetailLoading(true)
    try {
      const response = await api.getFinalVideo(video.workspace_id, video.id)
      setVideoDetail(response.data)
    } catch (error) {
      message.error('Failed to fetch video details')
    } finally {
      setDetailLoading(false)
    }
  }

  const columns = [
    {
      title: 'Filename',
      dataIndex: 'filename',
      key: 'filename',
    },
    {
      title: 'Duration',
      dataIndex: 'duration_ms',
      key: 'duration_ms',
      render: (ms: number | null) => ms ? `${Math.floor(ms / 60000)}:${Math.floor((ms % 60000) / 1000).toString().padStart(2, '0')}` : '-',
    },
    {
      title: 'Size',
      dataIndex: 'file_size_bytes',
      key: 'file_size_bytes',
      render: (bytes: number | null) => bytes ? `${(bytes / (1024 * 1024)).toFixed(2)} MB` : '-',
    },
    {
      title: 'Douyin',
      key: 'douyin',
      render: (_: any, video: FinalVideo) => (
        <Tag color={video.publish_status?.douyin?.published ? 'green' : 'default'}>
          {video.publish_status?.douyin?.published ? 'Published' : 'Not Published'}
        </Tag>
      ),
    },
    {
      title: 'WeChat',
      key: 'wechat',
      render: (_: any, video: FinalVideo) => (
        <Tag color={video.publish_status?.wechat_channels?.published ? 'green' : 'default'}>
          {video.publish_status?.wechat_channels?.published ? 'Published' : 'Not Published'}
        </Tag>
      ),
    },
    {
      title: 'Created',
      dataIndex: 'created_at',
      key: 'created_at',
      render: (date: string) => new Date(date).toLocaleString(),
    },
    {
      title: 'Actions',
      key: 'actions',
      render: (_: any, video: FinalVideo) => (
        <Space>
          <Button size="small" icon={<PlayCircleOutlined />} onClick={() => handleViewDetail(video)}>
            Detail
          </Button>
          <Button size="small" icon={<DownloadOutlined />} onClick={() => handleDownload(video)}>
            Download
          </Button>
          <Button size="small" danger icon={<DeleteOutlined />} onClick={() => handleDelete(video)}>
            Delete
          </Button>
        </Space>
      ),
    },
  ]

  return (
    <div>
      <Card
        title="Final Videos"
        extra={
          <Select
            value={selectedWorkspace}
            onChange={setSelectedWorkspace}
            style={{ width: 200 }}
            placeholder="Select Workspace"
          >
            {workspaces.map((ws) => (
              <Option key={ws.id} value={ws.id}>{ws.name}</Option>
            ))}
          </Select>
        }
      >
        <Table
          columns={columns}
          dataSource={videos}
          rowKey="id"
          loading={loading}
          pagination={{ pageSize: 10 }}
        />
      </Card>

      <Modal
        title="Video Details"
        open={detailModalVisible}
        onCancel={() => {
          setDetailModalVisible(false)
          setSelectedVideo(null)
          setVideoDetail(null)
        }}
        footer={[
          <Button key="close" onClick={() => setDetailModalVisible(false)}>
            Close
          </Button>,
          selectedVideo && (
            <Button
              key="publish"
              type="primary"
              onClick={() => {
                setDetailModalVisible(false)
                window.location.href = `/publish?video=${selectedVideo.id}`
              }}
            >
              Publish
            </Button>
          ),
        ]}
      >
        {detailLoading ? (
          <div style={{ textAlign: 'center', padding: 40 }}>
            <Spin size="large" />
          </div>
        ) : videoDetail ? (
          <Descriptions column={1} bordered>
            <Descriptions.Item label="Filename">{videoDetail.filename}</Descriptions.Item>
            <Descriptions.Item label="Duration">
              {videoDetail.duration_ms ? `${Math.floor(videoDetail.duration_ms / 60000)}:${Math.floor((videoDetail.duration_ms % 60000) / 1000).toString().padStart(2, '0')}` : '-'}
            </Descriptions.Item>
            <Descriptions.Item label="Size">
              {videoDetail.file_size_bytes ? `${(videoDetail.file_size_bytes / (1024 * 1024)).toFixed(2)} MB` : '-'}
            </Descriptions.Item>
            <Descriptions.Item label="Order Requirements">{videoDetail.order_requirements || '-'}</Descriptions.Item>
            <Descriptions.Item label="Industry">{videoDetail.order_industry || '-'}</Descriptions.Item>
            <Descriptions.Item label="Product">{videoDetail.order_product || '-'}</Descriptions.Item>
            <Descriptions.Item label="Region">{videoDetail.order_region || '-'}</Descriptions.Item>
            <Descriptions.Item label="Douyin Status">
              <Tag color={videoDetail.publish_status?.douyin?.published ? 'green' : 'default'}>
                {videoDetail.publish_status?.douyin?.published ? 'Published' : 'Not Published'}
              </Tag>
            </Descriptions.Item>
            <Descriptions.Item label="WeChat Status">
              <Tag color={videoDetail.publish_status?.wechat_channels?.published ? 'green' : 'default'}>
                {videoDetail.publish_status?.wechat_channels?.published ? 'Published' : 'Not Published'}
              </Tag>
            </Descriptions.Item>
            <Descriptions.Item label="Created">
              {new Date(videoDetail.created_at).toLocaleString()}
            </Descriptions.Item>
          </Descriptions>
        ) : null}
      </Modal>
    </div>
  )
}

export default FinalVideos
