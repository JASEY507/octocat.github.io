exports.handler = async (event) => {
  const ip =
    event.headers["x-forwarded-for"] ||
    event.headers["client-ip"] ||
    "IP yok";

  let body = {};
  try {
    body = JSON.parse(event.body);
  } catch {}

  console.log("====== YENİ ZİYARET ======");
  console.log("IP:", ip);
  console.log("GELEN DATA:", body);

  return {
    statusCode: 200,
    body: JSON.stringify({ status: "ok" }),
  };
};
