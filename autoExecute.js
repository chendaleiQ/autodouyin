(async () => {
  await selectSerial();
  await openSerial(
    {
      baudRate: 115200,
      dataBits: 8,
      stopBits: 1,
      parity: "none",
      bufferSize: 1024,
      flowControl: "none",
      overTime: 200,
    },
    (data) => {

      console.log({ data });
    }
  );
  sendData({ hex: false, content: "初始化", loopSend: false });
})();
