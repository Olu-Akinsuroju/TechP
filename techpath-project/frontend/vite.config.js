import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import path from 'path' // Import path module

// https://vitejs.dev/config/
export default defineConfig({
  // root: '.', // Explicitly set root to current dir (where vite.config.js is)
  plugins: [react()],
  build: {
    rollupOptions: {
      input: path.resolve(__dirname, 'public/index.html'), // Absolute path to index.html
    },
  },
})
