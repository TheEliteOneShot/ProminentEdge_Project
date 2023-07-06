import config from '/@src/config';

const getUploadedCadFilesRoute = config.routes.baseApi.getUploadedCadFiles;

export async function getUploadedCadFiles() {
    return await fetch(getUploadedCadFilesRoute)
    .then(response => response.json())
    .catch(() => console.error(`There was an error fetching getUploadedCadFiles`));
}
