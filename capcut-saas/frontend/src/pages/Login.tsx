import React, { useState } from 'react'
import { Form, Input, Button, Card, message } from 'antd'
import { UserOutlined, LockOutlined } from '@ant-design/icons'
import { api } from '../services/api'

interface LoginProps {
  onLogin: () => void
}

const Login: React.FC<LoginProps> = ({ onLogin }) => {
  const [isRegister, setIsRegister] = useState(false)
  const [loading, setLoading] = useState(false)

  const handleSubmit = async (values: { email: string; password: string; fullName?: string }) => {
    setLoading(true)
    try {
      if (isRegister) {
        await api.register(values.email, values.password, values.fullName)
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
      <Card title={isRegister ? 'Register' : 'Login'} style={{ width: 400 }}>
        <Form onFinish={handleSubmit} layout="vertical">
          {isRegister && (
            <Form.Item name="fullName" label="Full Name">
              <Input prefix={<UserOutlined />} placeholder="Full Name" />
            </Form.Item>
          )}
          <Form.Item name="email" label="Email" rules={[{ required: true, type: 'email' }]}>
            <Input prefix={<UserOutlined />} placeholder="Email" />
          </Form.Item>
          <Form.Item name="password" label="Password" rules={[{ required: true }]}>
            <Input.Password prefix={<LockOutlined />} placeholder="Password" />
          </Form.Item>
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
