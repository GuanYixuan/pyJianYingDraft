import React, { useState, useEffect } from 'react'
import { Card, Button, Space, Tag, message, Modal, Descriptions, Spin, Result } from 'antd'
import { CheckCircleOutlined, CloseCircleOutlined, RocketOutlined } from '@ant-design/icons'
import { api } from '../services/api'
import { useSearchParams } from 'react-router-dom'

interface FinalVideo {
  id: string
  workspace_id: string
  filename: string
  publish_status: {
    douyin: { published: boolean; video_id?: string; url?: string }
    wechat_channels: { published: boolean; video_id?: string; url?: string }
  }
}

const Publish: React.FC = () => {
  const [searchParams] = useSearchParams()
  const videoId = searchParams.get('video')
  const [video, setVideo] = useState<FinalVideo | null>(null)
  const [loading, setLoading] = useState(false)
  const [publishing, setPublishing] = useState<string | null>(null)
  const [publishStatus, setPublishStatus] = useState<any>(null)

  useEffect(() => {
    if (videoId) {
      fetchVideoAndStatus()
    }
  }, [videoId])

  const fetchVideoAndStatus = async () => {
    if (!videoId) return
    setLoading(true)
    try {
      // Get workspace first (we need it for the API call)
      const wsResponse = await api.getWorkspaces()
      if (wsResponse.data.length > 0) {
        const videoResponse = await api.getFinalVideo(wsResponse.data[0].id, videoId)
        setVideo(videoResponse.data)
        await fetchPublishStatus()
      }
    } catch (error) {
      message.error('Failed to fetch video')
    } finally {
      setLoading(false)
    }
  }

  const fetchPublishStatus = async () => {
    if (!videoId) return
    try {
      const response = await api.getPublishStatus(videoId)
      setPublishStatus(response.data)
    } catch (error) {
      console.error('Failed to fetch publish status')
    }
  }

  const handlePublish = async (platform: 'douyin' | 'wechat_channels') => {
    if (!videoId) return

    Modal.confirm({
      title: `Publish to ${platform === 'douyin' ? 'Douyin' : 'WeChat Channels'}`,
      content: `Are you sure you want to publish this video to ${platform === 'douyin' ? 'Douyin' : 'WeChat Channels'}?`,
      onOk: async () => {
        setPublishing(platform)
        try {
          if (platform === 'douyin') {
            await api.publishToDouyin(videoId)
          } else {
            await api.publishToWechatChannels(videoId)
          }
          message.success(`Video is being published to ${platform === 'douyin' ? 'Douyin' : 'WeChat Channels'}`)
          await fetchPublishStatus()
        } catch (error: any) {
          message.error(error.response?.data?.detail || `Failed to publish to ${platform}`)
        } finally {
          setPublishing(null)
        }
      },
    })
  }

  if (!videoId) {
    return (
      <Card title="Publish Video">
        <Result
          status="warning"
          title="No Video Selected"
          subTitle="Please select a video from the Final Videos page to publish."
        />
      </Card>
    )
  }

  if (loading) {
    return (
      <Card title="Publish Video">
        <div style={{ textAlign: 'center', padding: 40 }}>
          <Spin size="large" />
        </div>
      </Card>
    )
  }

  if (!video) {
    return (
      <Card title="Publish Video">
        <Result status="error" title="Video Not Found" />
      </Card>
    )
  }

  return (
    <div>
      <Card title="Publish Video">
        <Descriptions column={1} bordered style={{ marginBottom: 24 }}>
          <Descriptions.Item label="Filename">{video.filename}</Descriptions.Item>
        </Descriptions>

        <Card title="Publishing Status" type="inner">
          <Space direction="vertical" size="large" style={{ width: '100%' }}>
            {/* Douyin */}
            <Card size="small">
              <Space style={{ width: '100%', justifyContent: 'space-between' }}>
                <Space>
                  {publishStatus?.douyin?.published ? (
                    <CheckCircleOutlined style={{ color: 'green', fontSize: 20 }} />
                  ) : (
                    <CloseCircleOutlined style={{ color: 'gray', fontSize: 20 }} />
                  )}
                  <span style={{ fontSize: 16, fontWeight: 500 }}>Douyin (抖音)</span>
                </Space>
                {publishStatus?.douyin?.published ? (
                  <Space direction="vertical">
                    <Tag color="green">Published</Tag>
                    {publishStatus?.douyin?.url && (
                      <Button size="small" onClick={() => window.open(publishStatus.douyin.url, '_blank')}>
                        View on Douyin
                      </Button>
                    )}
                  </Space>
                ) : (
                  <Button
                    type="primary"
                    icon={<RocketOutlined />}
                    loading={publishing === 'douyin'}
                    onClick={() => handlePublish('douyin')}
                  >
                    Publish to Douyin
                  </Button>
                )}
              </Space>
            </Card>

            {/* WeChat Channels */}
            <Card size="small">
              <Space style={{ width: '100%', justifyContent: 'space-between' }}>
                <Space>
                  {publishStatus?.wechat_channels?.published ? (
                    <CheckCircleOutlined style={{ color: 'green', fontSize: 20 }} />
                  ) : (
                    <CloseCircleOutlined style={{ color: 'gray', fontSize: 20 }} />
                  )}
                  <span style={{ fontSize: 16, fontWeight: 500 }}>WeChat Channels (视频号)</span>
                </Space>
                {publishStatus?.wechat_channels?.published ? (
                  <Space direction="vertical">
                    <Tag color="green">Published</Tag>
                    {publishStatus?.wechat_channels?.url && (
                      <Button size="small" onClick={() => window.open(publishStatus.wechat_channels.url, '_blank')}>
                        View on WeChat
                      </Button>
                    )}
                  </Space>
                ) : (
                  <Button
                    type="primary"
                    icon={<RocketOutlined />}
                    loading={publishing === 'wechat_channels'}
                    onClick={() => handlePublish('wechat_channels')}
                  >
                    Publish to WeChat
                  </Button>
                )}
              </Space>
            </Card>
          </Space>
        </Card>
      </Card>
    </div>
  )
}

export default Publish
