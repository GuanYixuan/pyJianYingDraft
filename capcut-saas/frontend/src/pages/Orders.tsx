import React, { useState, useEffect } from 'react'
import { Table, Button, Modal, Form, Input, Select, Tag, Space, message, Card, Row, Col } from 'antd'
import { PlusOutlined } from '@ant-design/icons'
import { api } from '../services/api'

const { Option } = Select

interface Order {
  id: string
  user_id: string
  workspace_id: string
  requirements: string
  industry: string
  product: string
  region: string
  material_ids: string[]
  assigned_operator_id: string | null
  status: string
  priority: string
  ai_script: string | null
  created_at: string
}

interface Workspace {
  id: string
  name: string
  role: string
}

const statusColors: Record<string, string> = {
  pending: 'gold',
  assigned: 'blue',
  processing: 'processing',
  completed: 'green',
  failed: 'red',
}

const priorityColors: Record<string, string> = {
  low: 'default',
  normal: 'blue',
  high: 'orange',
  urgent: 'red',
}

const Orders: React.FC = () => {
  const [orders, setOrders] = useState<Order[]>([])
  const [workspaces, setWorkspaces] = useState<Workspace[]>([])
  const [loading, setLoading] = useState(false)
  const [modalVisible, setModalVisible] = useState(false)
  const [selectedWorkspace, setSelectedWorkspace] = useState<string | null>(null)
  const [form] = Form.useForm()

  useEffect(() => {
    fetchWorkspaces()
  }, [])

  useEffect(() => {
    if (selectedWorkspace) {
      fetchOrders(selectedWorkspace)
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

  const fetchOrders = async (workspaceId: string) => {
    setLoading(true)
    try {
      const response = await api.getOrders(workspaceId)
      setOrders(response.data)
    } catch (error) {
      message.error('Failed to fetch orders')
    } finally {
      setLoading(false)
    }
  }

  const handleCreateOrder = async (values: any) => {
    try {
      await api.createOrder({
        workspace_id: selectedWorkspace,
        requirements: values.requirements,
        industry: values.industry,
        product: values.product,
        region: values.region,
        material_ids: values.material_ids || [],
        priority: values.priority || 'normal',
      })
      message.success('Order created successfully')
      setModalVisible(false)
      form.resetFields()
      if (selectedWorkspace) {
        fetchOrders(selectedWorkspace)
      }
    } catch (error: any) {
      message.error(error.response?.data?.detail || 'Failed to create order')
    }
  }

  const columns = [
    {
      title: 'ID',
      dataIndex: 'id',
      key: 'id',
      ellipsis: true,
    },
    {
      title: 'Status',
      dataIndex: 'status',
      key: 'status',
      render: (status: string) => <Tag color={statusColors[status]}>{status.toUpperCase()}</Tag>,
    },
    {
      title: 'Priority',
      dataIndex: 'priority',
      key: 'priority',
      render: (priority: string) => <Tag color={priorityColors[priority]}>{priority.toUpperCase()}</Tag>,
    },
    {
      title: 'Industry',
      dataIndex: 'industry',
      key: 'industry',
    },
    {
      title: 'Product',
      dataIndex: 'product',
      key: 'product',
    },
    {
      title: 'Region',
      dataIndex: 'region',
      key: 'region',
    },
    {
      title: 'Requirements',
      dataIndex: 'requirements',
      key: 'requirements',
      ellipsis: true,
    },
    {
      title: 'Created',
      dataIndex: 'created_at',
      key: 'created_at',
      render: (date: string) => new Date(date).toLocaleDateString(),
    },
  ]

  return (
    <div>
      <Card
        title="Orders"
        extra={
          <Space>
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
            <Button type="primary" icon={<PlusOutlined />} onClick={() => setModalVisible(true)}>
              New Order
            </Button>
          </Space>
        }
      >
        <Row gutter={16} style={{ marginBottom: 16 }}>
          <Col span={4}>
            <Card size="small" title="Pending">{orders.filter(o => o.status === 'pending').length}</Card>
          </Col>
          <Col span={4}>
            <Card size="small" title="Assigned">{orders.filter(o => o.status === 'assigned').length}</Card>
          </Col>
          <Col span={4}>
            <Card size="small" title="Processing">{orders.filter(o => o.status === 'processing').length}</Card>
          </Col>
          <Col span={4}>
            <Card size="small" title="Completed">{orders.filter(o => o.status === 'completed').length}</Card>
          </Col>
          <Col span={4}>
            <Card size="small" title="Failed">{orders.filter(o => o.status === 'failed').length}</Card>
          </Col>
        </Row>
        <Table
          columns={columns}
          dataSource={orders}
          rowKey="id"
          loading={loading}
          pagination={{ pageSize: 10 }}
        />
      </Card>

      <Modal
        title="Create New Order"
        open={modalVisible}
        onCancel={() => {
          setModalVisible(false)
          form.resetFields()
        }}
        footer={null}
      >
        <Form form={form} onFinish={handleCreateOrder} layout="vertical">
          <Form.Item name="requirements" label="Requirements">
            <Input.TextArea rows={4} placeholder="Describe the video requirements..." />
          </Form.Item>
          <Form.Item name="industry" label="Industry">
            <Select allowClear placeholder="Select industry">
              <Option value="美妆">美妆</Option>
              <Option value="餐饮">餐饮</Option>
              <Option value="电商">电商</Option>
              <Option value="教育">教育</Option>
              <Option value="金融">金融</Option>
              <Option value="医疗">医疗</Option>
              <Option value="旅游">旅游</Option>
              <Option value="其他">其他</Option>
            </Select>
          </Form.Item>
          <Form.Item name="product" label="Product Name">
            <Input placeholder="Enter product name" />
          </Form.Item>
          <Form.Item name="region" label="Region">
            <Select allowClear placeholder="Select region">
              <Option value="华东">华东</Option>
              <Option value="华北">华北</Option>
              <Option value="华南">华南</Option>
              <Option value="华中">华中</Option>
              <Option value="西南">西南</Option>
              <Option value="西北">西北</Option>
              <Option value="东北">东北</Option>
            </Select>
          </Form.Item>
          <Form.Item name="priority" label="Priority">
            <Select defaultValue="normal">
              <Option value="low">Low</Option>
              <Option value="normal">Normal</Option>
              <Option value="high">High</Option>
              <Option value="urgent">Urgent</Option>
            </Select>
          </Form.Item>
          <Form.Item>
            <Button type="primary" htmlType="submit" block>
              Create Order
            </Button>
          </Form.Item>
        </Form>
      </Modal>
    </div>
  )
}

export default Orders
