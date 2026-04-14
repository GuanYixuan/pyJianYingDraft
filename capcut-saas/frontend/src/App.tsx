import React, { useState, useEffect } from 'react'
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom'
import { ConfigProvider, Layout, Menu, message } from 'antd'
import { DashboardOutlined, UploadOutlined, FileOutlined, VideoCameraOutlined } from '@ant-design/icons'
import Login from './pages/Login'
import Dashboard from './pages/Dashboard'
import Materials from './pages/Materials'
import Templates from './pages/Templates'
import Projects from './pages/Projects'
import DraftGenerator from './pages/DraftGenerator'
import { api } from './services/api'

const { Header, Sider, Content } = Layout

function App() {
  const [isAuthenticated, setIsAuthenticated] = useState(false)
  const [currentWorkspace, setCurrentWorkspace] = useState<string | null>(null)
  const [collapsed, setCollapsed] = useState(false)

  useEffect(() => {
    const token = localStorage.getItem('token')
    if (token) {
      setIsAuthenticated(true)
    }
  }, [])

  const handleLogout = () => {
    localStorage.removeItem('token')
    setIsAuthenticated(false)
    message.success('Logged out successfully')
  }

  const menuItems = [
    { key: '/dashboard', icon: <DashboardOutlined />, label: 'Dashboard' },
    { key: '/materials', icon: <UploadOutlined />, label: 'Materials' },
    { key: '/templates', icon: <FileOutlined />, label: 'Templates' },
    { key: '/projects', icon: <VideoCameraOutlined />, label: 'Projects' },
  ]

  if (!isAuthenticated) {
    return <Login onLogin={() => setIsAuthenticated(true)} />
  }

  return (
    <ConfigProvider
      theme={{
        token: {
          colorPrimary: '#00b42a',
        },
      }}
    >
      <BrowserRouter>
        <Layout style={{ minHeight: '100vh' }}>
          <Header style={{ color: 'white', fontSize: 20, display: 'flex', alignItems: 'center' }}>
            CapCut SaaS
          </Header>
          <Layout>
            <Sider collapsible collapsed={collapsed} onCollapse={setCollapsed}>
              <Menu theme="dark" mode="inline" items={menuItems} defaultSelectedKeys={['/dashboard']} />
            </Sider>
            <Content style={{ padding: 24 }}>
              <Routes>
                <Route path="/dashboard" element={<Dashboard />} />
                <Route path="/materials" element={<Materials />} />
                <Route path="/templates" element={<Templates />} />
                <Route path="/projects" element={<Projects />} />
                <Route path="/generate" element={<DraftGenerator />} />
                <Route path="*" element={<Navigate to="/dashboard" replace />} />
              </Routes>
            </Content>
          </Layout>
        </Layout>
      </BrowserRouter>
    </ConfigProvider>
  )
}

export default App
