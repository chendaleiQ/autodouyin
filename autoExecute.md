<meta charset="UTF-8">

# 执行文档

## 立即执行函数

所有代码都需要放在立即执行函数里面执行。

示例：

```
;(async ()=>{

    ...

})();
```

## 打开串口

示例：

```
await selectSerial();
```

## 选择串口

调用此函数时需要传入配置参数
示例：

```
await openSerial(
    {
      baudRate: 115200,// 波特率
      dataBits: 8, // 数据位
      stopBits: 1, // 停止位
      parity: "none", // 校验位
      bufferSize: 1024, // 缓冲区
      flowControl: "none", // 流控制
      overTime: 200, // 收超时时间
    },
    (data) => {
        // 在此可以对接收到的数据进行处理
        console.log({ data });
    }
  );
```

## 发送数据

可以使用此函数发送串口数据

示例：

```
  sendData({
    hex: false, // 是否是hex格式
    content: "初始化", // 发送内容
    loopSend: false, // 是否循环发送
    loopSendTime: 200, // 循环间隔时间
   });
```

## 完整示例

```
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

```