import React, { useState, useEffect } from 'react'
import { Card, Row, Col, Table, Tag, Space, Button, Statistic, message } from 'antd'
import { UserOutlined, ClockCircleOutlined, CheckCircleOutlined, ExclamationCircleOutlined } from '@ant-design/icons'
import { useNavigate } from 'react-router-dom'
import { api } from '../../services/api'

interface Order {
  id: string
  user_email: string
  user_full_name: string
  requirements: string
  industry: string
  product: string
  region: string
  status: string
  priority: string
  created_at: string
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

const OperatorDashboard: React.FC = () => {
  const [orders, setOrders] = useState<Order[]>([])
  const [loading, setLoading] = useState(false)
  const [stats, setStats] = useState({ total: 0, pending: 0, processing: 0, completed: 0 })
  const navigate = useNavigate()

  useEffect(() => {
    fetchOrders()
  }, [])

  const fetchOrders = async () => {
    setLoading(true)
    try {
      const response = await api.getOperatorOrders()
      setOrders(response.data)
      setStats({
        total: response.data.length,
        pending: response.data.filter((o: Order) => o.status === 'pending' || o.status === 'assigned').length,
        processing: response.data.filter((o: Order) => o.status === 'processing').length,
        completed: response.data.filter((o: Order) => o.status === 'completed').length,
      })
    } catch (error) {
      message.error('Failed to fetch orders')
    } finally {
      setLoading(false)
    }
  }

  const columns = [
    {
      title: 'Customer',
      key: 'customer',
      render: (_: any, order: Order) => (
        <Space direction="vertical" size={0}>
          <span>{order.user_full_name || 'N/A'}</span>
          <span style={{ color: '#888', fontSize: 12 }}>{order.user_email}</span>
        </Space>
      ),
    },
    {
      title: 'Requirements',
      dataIndex: 'requirements',
      key: 'requirements',
      ellipsis: true,
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
      title: 'Created',
      dataIndex: 'created_at',
      key: 'created_at',
      render: (date: string) => new Date(date).toLocaleDateString(),
    },
    {
      title: 'Actions',
      key: 'actions',
      render: (_: any, order: Order) => (
        <Button
          type="primary"
          size="small"
          onClick={() => navigate(`/operator/orders/${order.id}`)}
        >
          Process
        </Button>
      ),
    },
  ]

  return (
    <div>
      <Row gutter={16} style={{ marginBottom: 24 }}>
        <Col span={6}>
          <Card>
            <Statistic
              title="Total Orders"
              value={stats.total}
              prefix={<UserOutlined />}
            />
          </Card>
        </Col>
        <Col span={6}>
          <Card>
            <Statistic
              title="Pending/Assigned"
              value={stats.pending}
              prefix={<ClockCircleOutlined />}
              valueStyle={{ color: '#faad14' }}
            />
          </Card>
        </Col>
        <Col span={6}>
          <Card>
            <Statistic
              title="Processing"
              value={stats.processing}
              prefix={<ExclamationCircleOutlined />}
              valueStyle={{ color: '#1890ff' }}
            />
          </Card>
        </Col>
        <Col span={6}>
          <Card>
            <Statistic
              title="Completed"
              value={stats.completed}
              prefix={<CheckCircleOutlined />}
              valueStyle={{ color: '#52c41a' }}
            />
          </Card>
        </Col>
      </Row>

      <Card title="Orders to Process">
        <Table
          columns={columns}
          dataSource={orders}
          rowKey="id"
          loading={loading}
          pagination={{ pageSize: 10 }}
        />
      </Card>
    </div>
  )
}

export default OperatorDashboard
