import React, { useEffect, useState } from 'react'
import { Card, Row, Col, Statistic, List, Spin } from 'antd'
import { VideoCameraOutlined, UploadOutlined, FileOutlined, ProjectOutlined } from '@ant-design/icons'
import { api } from '../services/api'

interface Workspace {
  id: string
  name: string
  description?: string
  role: string
}

const Dashboard: React.FC = () => {
  const [workspaces, setWorkspaces] = useState<Workspace[]>([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    loadWorkspaces()
  }, [])

  const loadWorkspaces = async () => {
    try {
      const response = await api.getWorkspaces()
      setWorkspaces(response.data)
    } catch (error) {
      console.error('Failed to load workspaces:', error)
    } finally {
      setLoading(false)
    }
  }

  if (loading) {
    return <Spin size="large" style={{ display: 'flex', justifyContent: 'center', marginTop: 100 }} />
  }

  return (
    <div>
      <h1>Dashboard</h1>
      <Row gutter={16}>
        <Col span={6}>
          <Card>
            <Statistic title="Workspaces" value={workspaces.length} prefix={<ProjectOutlined />} />
          </Card>
        </Col>
        <Col span={6}>
          <Card>
            <Statistic title="Total Projects" value={0} prefix={<VideoCameraOutlined />} />
          </Card>
        </Col>
        <Col span={6}>
          <Card>
            <Statistic title="Total Materials" value={0} prefix={<UploadOutlined />} />
          </Card>
        </Col>
        <Col span={6}>
          <Card>
            <Statistic title="Templates" value={0} prefix={<FileOutlined />} />
          </Card>
        </Col>
      </Row>

      <h2 style={{ marginTop: 32 }}>Your Workspaces</h2>
      <List
        grid={{ gutter: 16, xs: 1, sm: 2, md: 2, lg: 3 }}
        dataSource={workspaces}
        renderItem={(workspace) => (
          <List.Item>
            <Card title={workspace.name} extra={<span style={{ color: '#999' }}>{workspace.role}</span>}>
              <p>{workspace.description || 'No description'}</p>
            </Card>
          </List.Item>
        )}
      />

      {workspaces.length === 0 && (
        <Card style={{ textAlign: 'center', marginTop: 32 }}>
          <p>No workspaces yet. Create one to get started!</p>
        </Card>
      )}
    </div>
  )
}

export default Dashboard
