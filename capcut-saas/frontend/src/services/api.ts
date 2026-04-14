import axios from 'axios'

const API_BASE = import.meta.env.VITE_API_URL || '/api/v1'

const axiosInstance = axios.create({
  baseURL: API_BASE,
  headers: {
    'Content-Type': 'application/json',
  },
})

// Add auth token to requests
axiosInstance.interceptors.request.use((config) => {
  const token = localStorage.getItem('token')
  if (token) {
    config.headers.Authorization = `Bearer ${token}`
  }
  return config
})

// Handle auth errors
axiosInstance.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      localStorage.removeItem('token')
      window.location.href = '/'
    }
    return Promise.reject(error)
  }
)

export const api = {
  // Auth
  login: (email: string, password: string) =>
    axiosInstance.post('/auth/login', { username: email, password }),

  register: (email: string, password: string, fullName?: string, industry?: string, product?: string, region?: string) =>
    axiosInstance.post('/auth/register', {
      email,
      password,
      full_name: fullName,
      industry,
      product,
      region,
    }),

  getMe: () => axiosInstance.get('/auth/me'),

  // Workspaces
  getWorkspaces: () => axiosInstance.get('/workspaces'),

  createWorkspace: (name: string, description?: string) =>
    axiosInstance.post('/workspaces', { name, description }),

  // Materials
  getMaterials: (workspaceId: string) =>
    axiosInstance.get(`/workspaces/${workspaceId}/materials`),

  uploadMaterial: (workspaceId: string, file: File, projectId?: string) => {
    const formData = new FormData()
    formData.append('file', file)
    if (projectId) formData.append('project_id', projectId)
    return axiosInstance.post(`/workspaces/${workspaceId}/materials/upload`, formData, {
      headers: { 'Content-Type': 'multipart/form-data' },
    })
  },

  deleteMaterial: (workspaceId: string, materialId: string) =>
    axiosInstance.delete(`/workspaces/${workspaceId}/materials/${materialId}`),

  // Templates
  getTemplates: (workspaceId: string) =>
    axiosInstance.get(`/workspaces/${workspaceId}/templates`),

  getTemplate: (workspaceId: string, templateId: string) =>
    axiosInstance.get(`/workspaces/${workspaceId}/templates/${templateId}`),

  createTemplate: (workspaceId: string, data: any) =>
    axiosInstance.post(`/workspaces/${workspaceId}/templates`, data),

  deleteTemplate: (workspaceId: string, templateId: string) =>
    axiosInstance.delete(`/workspaces/${workspaceId}/templates/${templateId}`),

  // Projects
  getProjects: (workspaceId: string) =>
    axiosInstance.get(`/workspaces/${workspaceId}/projects`),

  createProject: (workspaceId: string, name: string, description?: string) =>
    axiosInstance.post(`/workspaces/${workspaceId}/projects`, { name, description }),

  // Drafts
  getDrafts: (workspaceId: string, projectId: string) =>
    axiosInstance.get(`/workspaces/${workspaceId}/projects/${projectId}/drafts`),

  generateDraft: (workspaceId: string, projectId: string, data: any) =>
    axiosInstance.post(`/workspaces/${workspaceId}/projects/${projectId}/drafts/generate`, data),

  getDraft: (workspaceId: string, projectId: string, draftId: string) =>
    axiosInstance.get(`/workspaces/${workspaceId}/projects/${projectId}/drafts/${draftId}`),

  exportDraft: (workspaceId: string, projectId: string, draftId: string) =>
    axiosInstance.get(`/workspaces/${workspaceId}/projects/${projectId}/drafts/${draftId}/export`),

  deleteDraft: (workspaceId: string, projectId: string, draftId: string) =>
    axiosInstance.delete(`/workspaces/${workspaceId}/projects/${projectId}/drafts/${draftId}`),

  // Orders
  getOrders: (workspaceId?: string, status?: string) => {
    const params = new URLSearchParams()
    if (workspaceId) params.append('workspace_id', workspaceId)
    if (status) params.append('status_filter', status)
    return axiosInstance.get('/orders', { params })
  },

  createOrder: (data: {
    workspace_id: string
    requirements?: string
    industry?: string
    product?: string
    region?: string
    material_ids?: string[]
    priority?: string
  }) => axiosInstance.post('/orders', data),

  getOrder: (orderId: string) => axiosInstance.get(`/orders/${orderId}`),

  getOrderMaterials: (orderId: string) => axiosInstance.get(`/orders/${orderId}/materials`),

  // Operator
  getOperatorOrders: (status?: string) => {
    const params = new URLSearchParams()
    if (status) params.append('status_filter', status)
    return axiosInstance.get('/operator/orders', { params })
  },

  getOperatorOrder: (orderId: string) => axiosInstance.get(`/operator/orders/${orderId}`),

  getOperatorOrderMaterials: (orderId: string) =>
    axiosInstance.get(`/operator/orders/${orderId}/materials`),

  updateOrderStatus: (orderId: string, status: string) =>
    axiosInstance.patch(`/orders/${orderId}/status`, { status }),

  updateAiScript: (orderId: string, script: string) =>
    axiosInstance.patch(`/operator/orders/${orderId}/ai-script`, script),

  assignOperator: (orderId: string, operatorId: string) =>
    axiosInstance.post(`/orders/${orderId}/assign`, { operator_id: operatorId }),

  // Final Videos
  getFinalVideos: (workspaceId: string, orderId?: string) => {
    const params = new URLSearchParams()
    if (orderId) params.append('order_id', orderId)
    return axiosInstance.get(`/workspaces/${workspaceId}/final-videos`, { params })
  },

  getFinalVideo: (workspaceId: string, videoId: string) =>
    axiosInstance.get(`/workspaces/${workspaceId}/final-videos/${videoId}`),

  getFinalVideoDownloadUrl: (videoId: string) =>
    axiosInstance.get(`/final-videos/${videoId}/download`),

  deleteFinalVideo: (videoId: string) =>
    axiosInstance.delete(`/final-videos/${videoId}`),

  // Publish
  publishToDouyin: (videoId: string) =>
    axiosInstance.post(`/final-videos/${videoId}/publish/douyin`),

  publishToWechatChannels: (videoId: string) =>
    axiosInstance.post(`/final-videos/${videoId}/publish/wechat-channels`),

  getPublishStatus: (videoId: string) =>
    axiosInstance.get(`/final-videos/${videoId}/publish-status`),

  getPublishHistory: (videoId: string) =>
    axiosInstance.get(`/final-videos/${videoId}/publish-history`),
}

export default api
