import React, { useState } from 'react'
import { Upload, Card, List, Button, message, Modal, Select, Space } from 'antd'
import { InboxOutlined, DeleteOutlined } from '@ant-design/icons'
import { api } from '../services/api'

const { Dragger } = Upload

const Materials: React.FC = () => {
  const [materials, setMaterials] = useState<any[]>([])
  const [loading, setLoading] = useState(false)
  const [workspaceId] = useState<string>('default') // In production, get from context

  const loadMaterials = async () => {
    setLoading(true)
    try {
      const response = await api.getMaterials(workspaceId)
      setMaterials(response.data)
    } catch (error) {
      message.error('Failed to load materials')
    } finally {
      setLoading(false)
    }
  }

  const handleUpload = async (file: File) => {
    try {
      await api.uploadMaterial(workspaceId, file)
      message.success('Material uploaded successfully')
      loadMaterials()
    } catch (error) {
      message.error('Failed to upload material')
    }
    return false // Prevent default upload
  }

  const handleDelete = async (materialId: string) => {
    try {
      await api.deleteMaterial(workspaceId, materialId)
      message.success('Material deleted')
      loadMaterials()
    } catch (error) {
      message.error('Failed to delete material')
    }
  }

  return (
    <div>
      <h1>Materials</h1>

      <Card style={{ marginBottom: 24 }}>
        <Dragger accept="video/*,audio/*,image/*" beforeUpload={handleUpload} showUploadList={false}>
          <p className="ant-upload-drag-icon">
            <InboxOutlined />
          </p>
          <p className="ant-upload-text">Click or drag files to upload</p>
          <p className="ant-upload-hint">Support for video, audio, and images</p>
        </Dragger>
      </Card>

      <Card title="Your Materials">
        <List
          loading={loading}
          dataSource={materials}
          renderItem={(material) => (
            <List.Item
              actions={[
                <Button
                  key="delete"
                  type="text"
                  danger
                  icon={<DeleteOutlined />}
                  onClick={() => handleDelete(material.id)}
                >
                  Delete
                </Button>,
              ]}
            >
              <List.Item.Meta
                title={material.original_filename || material.filename}
                description={`Type: ${material.type} | Size: ${(material.file_size_bytes / 1024 / 1024).toFixed(2)} MB`}
              />
            </List.Item>
          )}
        />
      </Card>
    </div>
  )
}

export default Materials
