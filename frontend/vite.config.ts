import tailwindcss from '@tailwindcss/vite';
import react from '@vitejs/plugin-react';
import path from 'path';
import {defineConfig, loadEnv} from 'vite';

export default defineConfig(({mode}) => {
  const env = loadEnv(mode, '.', '');
  const pollingEnabled = process.env.CHOKIDAR_USEPOLLING === 'true';

  return {
    plugins: [react(), tailwindcss()],
    define: {
      'process.env.GEMINI_API_KEY': JSON.stringify(env.GEMINI_API_KEY),
    },
    resolve: {
      alias: {
        '@': path.resolve(__dirname, '.'),
      },
    },
    server: {
      host: '0.0.0.0',
      port: Number(process.env.VITE_PORT || 3000),
      strictPort: true,
      hmr: process.env.DISABLE_HMR !== 'true',
      watch: pollingEnabled
        ? {
            usePolling: true,
            interval: Number(process.env.CHOKIDAR_INTERVAL || 300),
          }
        : undefined,
    },
  };
});
