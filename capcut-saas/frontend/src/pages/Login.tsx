import React, { useState } from 'react'
import { Form, Input, Button, Card, message, Select, Divider } from 'antd'
import { UserOutlined, LockOutlined, ShopOutlined, EnvironmentOutlined } from '@ant-design/icons'
import { api } from '../services/api'

interface LoginProps {
  onLogin: () => void
}

const Login: React.FC<LoginProps> = ({ onLogin }) => {
  const [isRegister, setIsRegister] = useState(false)
  const [loading, setLoading] = useState(false)

  const handleSubmit = async (values: {
    email: string
    password: string
    fullName?: string
    industry?: string
    product?: string
    region?: string
  }) => {
    setLoading(true)
    try {
      if (isRegister) {
        await api.register(
          values.email,
          values.password,
          values.fullName,
          values.industry,
          values.product,
          values.region
        )
        message.success('Registration successful! Please login.')
        setIsRegister(false)
      } else {
        const response = await api.login(values.email, values.password)
        localStorage.setItem('token', response.data.access_token)
        message.success('Login successful!')
        onLogin()
      }
    } catch (error: any) {
      message.error(error.response?.data?.detail || 'An error occurred')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', minHeight: '100vh', background: '#f0f2f5' }}>
      <Card title={isRegister ? 'Register' : 'Login'} style={{ width: 450 }}>
        <Form onFinish={handleSubmit} layout="vertical">
          {isRegister && (
            <>
              <Form.Item name="fullName" label="Full Name">
                <Input prefix={<UserOutlined />} placeholder="Full Name" />
              </Form.Item>
              <Form.Item name="industry" label="Industry">
                <Select allowClear placeholder="Select your industry">
                  <Select.Option value="美妆">美妆</Select.Option>
                  <Select.Option value="餐饮">餐饮</Select.Option>
                  <Select.Option value="电商">电商</Select.Option>
                  <Select.Option value="教育">教育</Select.Option>
                  <Select.Option value="金融">金融</Select.Option>
                  <Select.Option value="医疗">医疗</Select.Option>
                  <Select.Option value="旅游">旅游</Select.Option>
                  <Select.Option value="其他">其他</Select.Option>
                </Select>
              </Form.Item>
              <Form.Item name="product" label="Product Name">
                <Input prefix={<ShopOutlined />} placeholder="Your main product" />
              </Form.Item>
              <Form.Item name="region" label="Region">
                <Select allowClear placeholder="Select your region">
                  <Select.Option value="华东">华东</Select.Option>
                  <Select.Option value="华北">华北</Select.Option>
                  <Select.Option value="华南">华南</Select.Option>
                  <Select.Option value="华中">华中</Select.Option>
                  <Select.Option value="西南">西南</Select.Option>
                  <Select.Option value="西北">西北</Select.Option>
                  <Select.Option value="东北">东北</Select.Option>
                </Select>
              </Form.Item>
            </>
          )}
          <Form.Item name="email" label="Email" rules={[{ required: true, type: 'email' }]}>
            <Input prefix={<UserOutlined />} placeholder="Email" />
          </Form.Item>
          <Form.Item name="password" label="Password" rules={[{ required: true }]}>
            <Input.Password prefix={<LockOutlined />} placeholder="Password" />
          </Form.Item>
          <Divider />
          <Form.Item>
            <Button type="primary" htmlType="submit" loading={loading} block>
              {isRegister ? 'Register' : 'Login'}
            </Button>
          </Form.Item>
          <Form.Item>
            <Button type="link" onClick={() => setIsRegister(!isRegister)} block>
              {isRegister ? 'Already have an account? Login' : "Don't have an account? Register"}
            </Button>
          </Form.Item>
        </Form>
      </Card>
    </div>
  )
}

export default Login
