exports.handler = async (event) => {
  const ip =
    event.headers["x-forwarded-for"] ||
    event.headers["client-ip"] ||
    "unknown";

  const ua = event.headers["user-agent"];
  const body = JSON.parse(event.body || "{}");

  console.log("IP:", ip);
  console.log("UA:", ua);
  console.log("DATA:", body);

  return {
    statusCode: 200,
    body: JSON.stringify({ ok: true })
  };
};

