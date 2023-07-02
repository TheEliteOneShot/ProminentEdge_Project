import config from '/@src/config';

const testItemRoute = config.routes.baseApi.testItem;

export async function getTestItems() {
    return await fetch(testItemRoute)
    .then(response => response.json())
    .catch(() => console.error(`There was an error fetching testItemRoute`));
}
