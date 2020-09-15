#使用方法

**示例：**
>python json_deal.py ./json_src.txt

**模板：**
>python json_deal [存储json文件的路径，默认为"./json_src.txt"]

**存储格式：**

文件会忽略 "\t", "\r", "\n", " " 读取json文件(类似下面的就行)

```json
{"oes":[{"label":"01","oe_num":1,"seq_num":1,"std_name":"多媒体播放器","price_4s":26100.010000,"oe_id":724967,"oe_code":"65 12
9 351 688","oe_name":"DVD 音频播放器
后座区","product_period":"_201407","sa_code1":3304890,"filter":false,"md5":"F38937D2BDECF6EF10616788A757D47D","replace_oe_id":726694},{"label":"01","oe_num":1,"seq_num":2,"std_name":"多媒体播放器","price_4s":26100.010000,"oe_id":726694,"oe_code":"65
12 9 365 772","oe_name":"DVD 音频播放器
后座区","product_period":"_201608","sa_code1":3304890,"filter":false,"md5":"6050BF6E1F43220FBE1E96DA1C9362F7","replace_oe_id":726992},{"label":"01","oe_num":1,"seq_num":3,"std_name":"多媒体播放器","price_4s":29400,"oe_id":726992,"oe_code":"65
12 9 368 387","oe_name":"DVD 音频播放器
后座区","product_period":"_201608","sa_code1":3304890,"filter":false,"md5":"59D8A0632F702C4DA33DE05ED5DF83D4"},{"label":"01","oe_num":1,"seq_num":4,"std_name":"多媒体播放器","price_4s":22700.010000,"oe_id":718660,"oe_code":"65
12 9 291 376","oe_name":"保修 DVD 音频播放器
后座区","product_period":"_201608","sa_code1":3304890,"filter":false,"md5":"8CB56B7955DDA388840F1A848BDBCEB2"},{"label":"02","oe_num":1,"seq_num":5,"std_name":"","price_4s":314,"oe_id":705222,"oe_code":"65
12 9 201
039","oe_name":"盖罩","product_period":"_201608","sa_code1":3304890,"filter":false,"md5":"28FAD7CF496E75F23C0127BDE5995D05"},{"label":"03","oe_num":1,"seq_num":6,"std_name":"卡扣","price_4s":55,"oe_id":697067,"oe_code":"65
83 9 165
318","oe_name":"调节元件","product_period":"_201608","sa_code1":3304890,"filter":false,"md5":"0628F5E557C398FE9C2EAC78E27D5B81"}],"catalog_sa":{"3304890":{"sa_code_info":[{"sa_code_opc":"
","textcode_text":"用于车辆及"},{"sa_code_opc":"+","sa_code_text":"S6FHA","textcode_text":"后座区视听设备
PROFESSIONAL"}],"filter":false}},"sizer":[{"opc":"+","code":"S6FHA","text":"后座区视听设备 PROFESSIONAL"}],"status":0}
```

**输出格式：**

```text
|参数名称|参数含义|类型|备注|
|:---|:---|:---|:---|
|oes| |array||
|oes::label| |string||
|oes::oe_num| |int||
|oes::seq_num| |int||
|oes::std_name| |string||
|oes::price_4s| |float||
|oes::oe_id| |int||
|oes::oe_code| |string||
|oes::oe_name| |string||
|oes::product_period| |string||
|oes::sa_code1| |int||
|oes::filter| |bool||
|oes::md5| |string||
|oes::replace_oe_id| |int||
|catalog_sa| |dict||
|catalog_sa::3304890| |dict||
|catalog_sa::3304890::sa_code_info| |array||
|catalog_sa::3304890::sa_code_info::sa_code_opc| |string||
|catalog_sa::3304890::sa_code_info::textcode_text| |string||
|catalog_sa::3304890::sa_code_info::sa_code_text| |string||
|catalog_sa::3304890::filter| |bool||
|sizer| |array||
|sizer::opc| |string||
|sizer::code| |string||
|sizer::text| |string||
|status| |int||

```
**输出展示：**

|参数名称|参数含义|类型|备注|
|:---|:---|:---|:---|
|oes| |array||
|oes::label| |string||
|oes::oe_num| |int||
|oes::seq_num| |int||
|oes::std_name| |string||
|oes::price_4s| |float||
|oes::oe_id| |int||
|oes::oe_code| |string||
|oes::oe_name| |string||
|oes::product_period| |string||
|oes::sa_code1| |int||
|oes::filter| |bool||
|oes::md5| |string||
|oes::replace_oe_id| |int||
|catalog_sa| |dict||
|catalog_sa::3304890| |dict||
|catalog_sa::3304890::sa_code_info| |array||
|catalog_sa::3304890::sa_code_info::sa_code_opc| |string||
|catalog_sa::3304890::sa_code_info::textcode_text| |string||
|catalog_sa::3304890::sa_code_info::sa_code_text| |string||
|catalog_sa::3304890::filter| |bool||
|sizer| |array||
|sizer::opc| |string||
|sizer::code| |string||
|sizer::text| |string||
|status| |int||
