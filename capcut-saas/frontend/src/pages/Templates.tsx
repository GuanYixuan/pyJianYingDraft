import React, { useState } from 'react'
import { Card, List, Button, Modal, Form, Input, Select, message, Upload } from 'antd'
import { PlusOutlined, DeleteOutlined, UploadOutlined } from '@ant-design/icons'
import { api } from '../services/api'

const Templates: React.FC = () => {
  const [templates, setTemplates] = useState<any[]>([])
  const [loading, setLoading] = useState(false)
  const [isModalOpen, setIsModalOpen] = useState(false)
  const [form] = Form.useForm()
  const [workspaceId] = useState<string>('default')

  const loadTemplates = async () => {
    setLoading(true)
    try {
      const response = await api.getTemplates(workspaceId)
      setTemplates(response.data)
    } catch (error) {
      message.error('Failed to load templates')
    } finally {
      setLoading(false)
    }
  }

  const handleCreate = async (values: any) => {
    try {
      // In production, this would upload a draft_content.json file
      await api.createTemplate(workspaceId, {
        ...values,
        content: {}, // Would be the actual draft JSON
      })
      message.success('Template created successfully')
      setIsModalOpen(false)
      form.resetFields()
      loadTemplates()
    } catch (error) {
      message.error('Failed to create template')
    }
  }

  const handleDelete = async (templateId: string) => {
    try {
      await api.deleteTemplate(workspaceId, templateId)
      message.success('Template deleted')
      loadTemplates()
    } catch (error) {
      message.error('Failed to delete template')
    }
  }

  return (
    <div>
      <h1>Templates</h1>

      <Card
        title="Your Templates"
        extra={
          <Button type="primary" icon={<PlusOutlined />} onClick={() => setIsModalOpen(true)}>
            Create Template
          </Button>
        }
      >
        <List
          loading={loading}
          dataSource={templates}
          renderItem={(template) => (
            <List.Item
              actions={[
                <Button key="delete" type="text" danger icon={<DeleteOutlined />} onClick={() => handleDelete(template.id)}>
                  Delete
                </Button>,
              ]}
            >
              <List.Item.Meta
                title={template.name}
                description={template.description || `Category: ${template.category || 'None'}`}
              />
            </List.Item>
          )}
        />
      </Card>

      <Modal title="Create Template" open={isModalOpen} onCancel={() => setIsModalOpen(false)} footer={null}>
        <Form form={form} layout="vertical" onFinish={handleCreate}>
          <Form.Item name="name" label="Template Name" rules={[{ required: true }]}>
            <Input />
          </Form.Item>
          <Form.Item name="description" label="Description">
            <Input.TextArea />
          </Form.Item>
          <Form.Item name="category" label="Category">
            <Select
              options={[
                { value: 'marketing', label: 'Marketing' },
                { value: 'social', label: 'Social Media' },
                { value: 'education', label: 'Education' },
              ]}
            />
          </Form.Item>
          <Form.Item>
            <Space>
              <Button type="primary" htmlType="submit">
                Create
              </Button>
              <Button onClick={() => setIsModalOpen(false)}>Cancel</Button>
            </Space>
          </Form.Item>
        </Form>
      </Modal>
    </div>
  )
}

export default Templates
