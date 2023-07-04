import config from '/@src/config';

const getWeatherPointDataRoute = config.routes.baseApi.getWeatherPointData;

export async function getWeatherPointData(lat: any, lon: any, start: any, end: any) {
    return await fetch(`${getWeatherPointDataRoute}?lat=${lat}&lon=${lon}&start=${start}&end=${end}`, {
    method: "GET",
    headers: {
        'X-RapidAPI-Key': config.RAPID_API_KEY,
        'X-RapidAPI-Host': config.RAPID_API_HOST
        },
    })
    .then(response => response.json())
    .catch(() => console.error(`There was an error fetching getWeatherPointData`));
}
