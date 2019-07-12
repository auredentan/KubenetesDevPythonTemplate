
export const test = async () => {
    console.log("Calling test");
    let response = await fetch("/api/test");
    let data = await response.json();
    console.log("Received data", data);
    return data;
}