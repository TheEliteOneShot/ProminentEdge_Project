import config from '/@src/config';

const getApparatusInformationByCadFileIDRoute = config.routes.baseApi.getApparatusInformationByCadFileID;

export async function getApparatusInformationByCadFileID(cadfile_id: number) {
    return await fetch(getApparatusInformationByCadFileIDRoute + `?cadfileid=${cadfile_id}` )
    .then(response => response.json())
    .catch(() => console.error(`There was an error fetching getApparatusInformationByCadFileID`));
}
