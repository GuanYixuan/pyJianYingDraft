import React, { useState, useEffect } from 'react'
import { Card, Descriptions, Tag, Space, Button, Table, message, Upload, Modal, Form, Input, Select, Spin, Timeline } from 'antd'
import { DownloadOutlined, UploadOutlined, CheckCircleOutlined, PlayCircleOutlined } from '@ant-design/icons'
import { useParams, useNavigate } from 'react-router-dom'
import { api } from '../../services/api'

const { Option } = Select

interface Material {
  id: string
  filename: string
  original_filename: string
  type: string
  file_size_bytes: number
  download_url: string
  cdn_url: string
}

interface OrderDetail {
  id: string
  user_email: string
  user_full_name: string
  requirements: string
  industry: string
  product: string
  region: string
  status: string
  priority: string
  ai_script: string | null
  material_ids: string[]
  created_at: string
}

const statusColors: Record<string, string> = {
  pending: 'gold',
  assigned: 'blue',
  processing: 'processing',
  completed: 'green',
  failed: 'red',
}

const OrderProcess: React.FC = () => {
  const { orderId } = useParams<{ orderId: string }>()
  const navigate = useNavigate()
  const [order, setOrder] = useState<OrderDetail | null>(null)
  const [materials, setMaterials] = useState<Material[]>([])
  const [loading, setLoading] = useState(true)
  const [updating, setUpdating] = useState(false)
  const [scriptModalVisible, setScriptModalVisible] = useState(false)
  const [uploadModalVisible, setUploadModalVisible] = useState(false)
  const [aiScript, setAiScript] = useState('')
  const [form] = Form.useForm()

  useEffect(() => {
    if (orderId) {
      fetchOrderDetail()
    }
  }, [orderId])

  const fetchOrderDetail = async () => {
    if (!orderId) return
    setLoading(true)
    try {
      const response = await api.getOperatorOrder(orderId)
      setOrder(response.data)
      setAiScript(response.data.ai_script || '')
      await fetchMaterials()
    } catch (error) {
      message.error('Failed to fetch order details')
    } finally {
      setLoading(false)
    }
  }

  const fetchMaterials = async () => {
    if (!orderId) return
    try {
      const response = await api.getOperatorOrderMaterials(orderId)
      setMaterials(response.data)
    } catch (error) {
      console.error('Failed to fetch materials')
    }
  }

  const handleUpdateStatus = async (newStatus: string) => {
    if (!orderId) return
    setUpdating(true)
    try {
      await api.updateOrderStatus(orderId, newStatus)
      message.success(`Status updated to ${newStatus}`)
      await fetchOrderDetail()
    } catch (error: any) {
      message.error(error.response?.data?.detail || 'Failed to update status')
    } finally {
      setUpdating(false)
    }
  }

  const handleUpdateScript = async () => {
    if (!orderId) return
    setUpdating(true)
    try {
      await api.updateAiScript(orderId, aiScript)
      message.success('AI script updated')
      setScriptModalVisible(false)
    } catch (error: any) {
      message.error(error.response?.data?.detail || 'Failed to update script')
    } finally {
      setUpdating(false)
    }
  }

  const handleUploadFinalVideo = async (values: any) => {
    if (!orderId) return
    setUpdating(true)
    try {
      // The file upload needs to be handled differently
      // For now, we just show a placeholder
      message.info('Video upload feature coming soon')
      setUploadModalVisible(false)
    } catch (error: any) {
      message.error(error.response?.data?.detail || 'Failed to upload video')
    } finally {
      setUpdating(false)
    }
  }

  const materialColumns = [
    {
      title: 'Filename',
      dataIndex: 'filename',
      key: 'filename',
    },
    {
      title: 'Type',
      dataIndex: 'type',
      key: 'type',
    },
    {
      title: 'Size',
      dataIndex: 'file_size_bytes',
      key: 'file_size_bytes',
      render: (bytes: number) => `${(bytes / (1024 * 1024)).toFixed(2)} MB`,
    },
    {
      title: 'Actions',
      key: 'actions',
      render: (_: any, material: Material) => (
        <Space>
          {material.download_url && (
            <Button
              size="small"
              icon={<DownloadOutlined />}
              onClick={() => window.open(material.download_url, '_blank')}
            >
              Download
            </Button>
          )}
          {material.cdn_url && (
            <Button
              size="small"
              icon={<PlayCircleOutlined />}
              onClick={() => window.open(material.cdn_url, '_blank')}
            >
              Preview
            </Button>
          )}
        </Space>
      ),
    },
  ]

  if (loading) {
    return (
      <div style={{ textAlign: 'center', padding: 60 }}>
        <Spin size="large" />
      </div>
    )
  }

  if (!order) {
    return <Card>Order not found</Card>
  }

  return (
    <div>
      <Card
        title="Order Details"
        extra={
          <Space>
            <Tag color={statusColors[order.status]} style={{ fontSize: 16 }}>
              {order.status.toUpperCase()}
            </Tag>
          </Space>
        }
        actions={[
          <Button
            key="assigned"
            onClick={() => handleUpdateStatus('assigned')}
            loading={updating}
            disabled={order.status !== 'pending'}
          >
            Mark Assigned
          </Button>,
          <Button
            key="processing"
            onClick={() => handleUpdateStatus('processing')}
            loading={updating}
            disabled={order.status !== 'assigned'}
          >
            Start Processing
          </Button>,
          <Button
            key="completed"
            type="primary"
            onClick={() => handleUpdateStatus('completed')}
            loading={updating}
            disabled={order.status !== 'processing'}
          >
            Mark Completed
          </Button>,
          <Button
            key="failed"
            danger
            onClick={() => handleUpdateStatus('failed')}
            loading={updating}
            disabled={order.status === 'completed'}
          >
            Mark Failed
          </Button>,
        ]}
      >
        <Descriptions column={2}>
          <Descriptions.Item label="Customer">{order.user_full_name || 'N/A'}</Descriptions.Item>
          <Descriptions.Item label="Email">{order.user_email}</Descriptions.Item>
          <Descriptions.Item label="Industry">{order.industry || '-'}</Descriptions.Item>
          <Descriptions.Item label="Product">{order.product || '-'}</Descriptions.Item>
          <Descriptions.Item label="Region">{order.region || '-'}</Descriptions.Item>
          <Descriptions.Item label="Priority">
            <Tag color={order.priority === 'urgent' ? 'red' : order.priority === 'high' ? 'orange' : 'blue'}>
              {order.priority.toUpperCase()}
            </Tag>
          </Descriptions.Item>
          <Descriptions.Item label="Created">
            {new Date(order.created_at).toLocaleString()}
          </Descriptions.Item>
        </Descriptions>
      </Card>

      <Card title="Requirements" style={{ marginTop: 16 }}>
        <p>{order.requirements || 'No requirements specified'}</p>
      </Card>

      <Card
        title="AI Script"
        style={{ marginTop: 16 }}
        extra={
          <Button onClick={() => setScriptModalVisible(true)}>
            {order.ai_script ? 'Edit Script' : 'Add Script'}
          </Button>
        }
      >
        {order.ai_script ? (
          <pre style={{ whiteSpace: 'pre-wrap', background: '#f5f5f5', padding: 16 }}>
            {order.ai_script}
          </pre>
        ) : (
          <p style={{ color: '#888' }}>No AI script generated yet</p>
        )}
      </Card>

      <Card title="Customer Materials" style={{ marginTop: 16 }}>
        <Table
          columns={materialColumns}
          dataSource={materials}
          rowKey="id"
          pagination={false}
        />
      </Card>

      <Card title="Actions" style={{ marginTop: 16 }}>
        <Space>
          <Button
            type="primary"
            icon={<UploadOutlined />}
            onClick={() => setUploadModalVisible(true)}
            disabled={order.status !== 'processing'}
          >
            Upload Final Video
          </Button>
        </Space>
      </Card>

      <Modal
        title="AI Script"
        open={scriptModalVisible}
        onCancel={() => setScriptModalVisible(false)}
        onOk={handleUpdateScript}
        okText="Save Script"
        confirmLoading={updating}
      >
        <Form.Item label="Script Content">
          <Input.TextArea
            rows={10}
            value={aiScript}
            onChange={(e) => setAiScript(e.target.value)}
            placeholder="Enter AI-generated script..."
          />
        </Form.Item>
      </Modal>

      <Modal
        title="Upload Final Video"
        open={uploadModalVisible}
        onCancel={() => setUploadModalVisible(false)}
        footer={null}
      >
        <Form form={form} onFinish={handleUploadFinalVideo} layout="vertical">
          <Form.Item label="Video File">
            <Upload.Dragger
              beforeUpload={(file) => {
                const isVideo = file.type.startsWith('video/')
                if (!isVideo) {
                  message.error('You can only upload video files!')
                }
                return isVideo
              }}
              maxCount={1}
            >
              <p className="ant-upload-drag-icon">
                <UploadOutlined />
              </p>
              <p className="ant-upload-text">Click or drag video file to upload</p>
            </Upload.Dragger>
          </Form.Item>
          <Form.Item>
            <Button type="primary" htmlType="submit" block loading={updating}>
              Upload
            </Button>
          </Form.Item>
        </Form>
      </Modal>
    </div>
  )
}

export default OrderProcess
