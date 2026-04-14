import React, { useState, useEffect } from 'react'
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom'
import { ConfigProvider, Layout, Menu, message } from 'antd'
import { DashboardOutlined, UploadOutlined, FileOutlined, VideoCameraOutlined, ShoppingOutlined, VideoOutlined, RocketOutlined } from '@ant-design/icons'
import Login from './pages/Login'
import Dashboard from './pages/Dashboard'
import Materials from './pages/Materials'
import Templates from './pages/Templates'
import Projects from './pages/Projects'
import DraftGenerator from './pages/DraftGenerator'
import Orders from './pages/Orders'
import FinalVideos from './pages/FinalVideos'
import Publish from './pages/Publish'
import OperatorDashboard from './pages/operator/Dashboard'
import OrderProcess from './pages/operator/OrderProcess'
import { api } from './services/api'

const { Header, Sider, Content } = Layout

function App() {
  const [isAuthenticated, setIsAuthenticated] = useState(false)
  const [currentWorkspace, setCurrentWorkspace] = useState<string | null>(null)
  const [collapsed, setCollapsed] = useState(false)
  const [userRole, setUserRole] = useState<string | null>(null)

  useEffect(() => {
    const token = localStorage.getItem('token')
    if (token) {
      setIsAuthenticated(true)
      // Fetch user info to get role
      api.getMe()
        .then(res => setUserRole(res.data.role))
        .catch(() => {})
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
    { key: '/orders', icon: <ShoppingOutlined />, label: 'Orders' },
    { key: '/final-videos', icon: <VideoOutlined />, label: 'Final Videos' },
    { key: '/publish', icon: <RocketOutlined />, label: 'Publish' },
  ]

  // Add operator menu items if user is operator/admin
  if (userRole === 'operator' || userRole === 'admin') {
    menuItems.push(
      { type: 'divider' as const },
      { key: '/operator', icon: <DashboardOutlined />, label: 'Operator Panel', danger: true }
    )
  }

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
                <Route path="/orders" element={<Orders />} />
                <Route path="/final-videos" element={<FinalVideos />} />
                <Route path="/publish" element={<Publish />} />
                <Route path="/operator/dashboard" element={<OperatorDashboard />} />
                <Route path="/operator/orders/:orderId" element={<OrderProcess />} />
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
