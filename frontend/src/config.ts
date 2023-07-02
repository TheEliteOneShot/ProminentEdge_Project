const env = {
    API_BASE_PROTOCOL: import.meta.env.VITE_API_BASE_PROTOCOL,
    // @ts-ignore
    API_BASE_HOST: import.meta.env.VITE_API_BASE_HOST,
    // @ts-ignore
    API_BASE_PORT: import.meta.env.VITE_API_BASE_PORT,
    // @ts-ignore
    API_BASE_PREFIX: import.meta.env.VITE_API_BASE_PREFIX,
};

const routes = {
    baseUrl: `${env.API_BASE_PROTOCOL}://${env.API_BASE_HOST}:${env.API_BASE_PORT}${env.API_BASE_PREFIX}`,
    baseApi: {
      baseUrl: `${env.API_BASE_PROTOCOL}://${env.API_BASE_HOST}:${env.API_BASE_PORT}${env.API_BASE_PREFIX}/user`,
      testItem: `${env.API_BASE_PROTOCOL}://${env.API_BASE_HOST}:${env.API_BASE_PORT}${env.API_BASE_PREFIX}/test`,
    },
  };
  
const config = { ...env, routes };

export default config;
