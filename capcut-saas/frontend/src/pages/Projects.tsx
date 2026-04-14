import React, { useState } from 'react'
import { Card, List, Button, Modal, Form, Input, message } from 'antd'
import { PlusOutlined, PlayCircleOutlined } from '@ant-design/icons'
import { useNavigate } from 'react-router-dom'
import { api } from '../services/api'

const Projects: React.FC = () => {
  const [projects, setProjects] = useState<any[]>([])
  const [loading, setLoading] = useState(false)
  const [isModalOpen, setIsModalOpen] = useState(false)
  const [form] = Form.useForm()
  const [workspaceId] = useState<string>('default')
  const navigate = useNavigate()

  const loadProjects = async () => {
    setLoading(true)
    try {
      const response = await api.getProjects(workspaceId)
      setProjects(response.data)
    } catch (error) {
      message.error('Failed to load projects')
    } finally {
      setLoading(false)
    }
  }

  const handleCreate = async (values: { name: string; description?: string }) => {
    try {
      await api.createProject(workspaceId, values.name, values.description)
      message.success('Project created successfully')
      setIsModalOpen(false)
      form.resetFields()
      loadProjects()
    } catch (error) {
      message.error('Failed to create project')
    }
  }

  return (
    <div>
      <h1>Projects</h1>

      <Card
        title="Your Projects"
        extra={
          <Button type="primary" icon={<PlusOutlined />} onClick={() => setIsModalOpen(true)}>
            Create Project
          </Button>
        }
      >
        <List
          loading={loading}
          dataSource={projects}
          renderItem={(project) => (
            <List.Item
              actions={[
                <Button
                  key="generate"
                  type="link"
                  icon={<PlayCircleOutlined />}
                  onClick={() => navigate('/generate', { state: { projectId: project.id } })}
                >
                  Generate Draft
                </Button>,
              ]}
            >
              <List.Item.Meta title={project.name} description={project.description || 'No description'} />
            </List.Item>
          )}
        />
      </Card>

      <Modal title="Create Project" open={isModalOpen} onCancel={() => setIsModalOpen(false)} footer={null}>
        <Form form={form} layout="vertical" onFinish={handleCreate}>
          <Form.Item name="name" label="Project Name" rules={[{ required: true }]}>
            <Input />
          </Form.Item>
          <Form.Item name="description" label="Description">
            <Input.TextArea />
          </Form.Item>
          <Form.Item>
            <Button type="primary" htmlType="submit">
              Create
            </Button>
          </Form.Item>
        </Form>
      </Modal>
    </div>
  )
}

export default Projects
