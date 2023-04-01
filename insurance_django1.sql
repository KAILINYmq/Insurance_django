/*
 Navicat Premium Data Transfer

 Source Server         : AL_Mongo
 Source Server Type    : MongoDB
 Source Server Version : 30424
 Source Host           : 121.43.189.184:27017
 Source Schema         : insurance_django

 Target Server Type    : MongoDB
 Target Server Version : 30424
 File Encoding         : 65001

 Date: 07/05/2020 22:01:01
*/


// ----------------------------
// Collection structure for insurance_data_fyj
// ----------------------------
db.getCollection("insurance_data_fyj").drop();
db.createCollection("insurance_data_fyj");

// ----------------------------
// Documents of insurance_data_fyj
// ----------------------------
db.getCollection("insurance_data_fyj").insert([ {
    _id: ObjectId("5eaf954818400000fe005237"),
    name: "福佑金生年金保险",
    username: 0,
    lable: [
        "4.025%定价利率",
        "第五年末即可领取",
        "生存总利益高"
    ],
    equity: [
        "复效:若因某些特殊原因未及时缴纳保费,导致保单停效,自停效之日起两年内,可办理相关手续使保单复效。",
        "犹豫期退保:犹豫期退保指投保人在合同约定的犹豫期内的退保。通常会扣除工本费后无息退还全部保费。",
        "退保:保险合同沒有完全履行时,经投保人和被保险人申请,保险人同意,解除双方由合同确定的法律关系,犹豫期后退保有损失,保险人按合同的约定退还保险单的现金价值。",
        "保单变更:在保单有效期内,经投保人和保险人协商同意,可以修改保单的有关内容。",
        "索赔:指当保险标的遭受承保责任范围内的风险损失或伤害时,被保险人/受益人有权向保险人提出索赔。",
        "保单贷款:指投保人将所持有的保单抵押给保险公司,按照保单现金价值的一定比例获得资金的一种借贷方式。由于质押贷款过程中客户的保险保障不受影响,所以保单依然有效。"
    ],
    notice: [
        "投保前请您仔细阅读：产品条款客户告知书保单样本查看费率表",
        "责任免除、保险责任、犹豫期、费用扣除、退保、保险单现金价值、投保人、被保险人义务等内容详见产品条款，请务必仔细阅读产品条款及电子保单的特别约定。",
        "本产品由海保人寿保险股份有限公司承保并负责理赔。海保人寿保险股份有限公司总部设在海南海口，暂无分支机构设立。",
        "本产品承保年龄为出生30天-65周岁（含第30天、含65周岁），且从事1-6类职业人士。",
        "本产品支持为本人、父母、配偶、子女投保，且投保人年龄需满足交费期满时小于等于70周岁。",
        "本产品最低保费限制为1000元，以1000元的整倍数递增，最高保费总额限制为1000万元。",
        "本产品不同承保年龄可选择的保障期限和缴费年限限制详见附件。",
        "本产品有15天的犹豫期。",
        "本产品不支持外籍人士投保。",
        "本产品提供电子保单。根据《中华人民共和国合同法》第十一条规定，数据电文是合法的合同表现形式，电子保单与纸质保单具有同等法律效力。完成购买后，我们会把电子保单发到您的邮箱。",
        "本产品报备文件编号：海保字[2018]121号。"
    ],
    sex: [
        "男",
        "女"
    ],
    insurantJob: [
        "1-6类"
    ],
    insurantDateLimit: [
        "10",
        "15",
        "20"
    ],
    paymentType: [
        "一次性",
        "年交"
    ],
    insureAgeLimit: [
        "趸交",
        "3年",
        "5年"
    ],
    premium: [
        {
            value: "1000-10000000",
            min: NumberInt("1000"),
            max: NumberInt("10000000"),
            step: NumberInt("1000")
        }
    ],
    coverageAreaName: [
        "海南省"
    ],
    "protect_interest": [
        {
            name: "生存保险金",
            fullPremium: "年交保费*对应的生存保险金给付比例",
            description: "在合同有效期内，自本合同生效后的第六个保单周年日起，至保险期满的前一个保单周年日（含当日），若被保险人于每个保单周年日零时仍生存，保险公司将于每个保单周年日按保险合同的基本保险金额所对应的年交保险费乘以对应的生存保险金给付比例给付生存保险金。给付比例详见<strong><a href=\"http://files.huizecdn.com/file1/M00/5A/CA/CgUA3F4dWHyAB4OhAABwKO6ghCw440.pdf\" target=\"_blank\">附件</a>。</strong>"
        },
        {
            name: "特别生存保险金",
            fullPremium: "年交保费*对应的特别生存保险金给付比例",
            description: "在合同有效期内，若被保险人于本合同生效后的第五个保单周年日零时仍生存，保险公司将于第五个保单周年日按保险合同的基本保险金额所对应的年交保险费乘以对应的特别生存保险金给付比例给付特别生存保险金，给付比例详见<a href=\"http://files.huizecdn.com/file1/M00/5A/CB/CgUA3F4dWJ6AZSs2AABy4zNd5_U832.pdf\" target=\"_blank\"><strong>附件</strong></a>。"
        },
        {
            name: "身故保险金",
            fullPremium: "累计已交保险费和身故时现金价值的较大值",
            description: "在合同有效期内，若被保险人身故，保险公司将按下列两者的较大值给付身故保险金，保险合同终止：<br />\r\n（1）本合同累计已交保险费（不含利息）；<br />\r\n（2）被保险人身故时本合同的现金价值"
        }
    ],
    "image_url": [
        "https://files.huizecdn.com/file1/M00/60/67/CgUA3F5PUyaAQGwSAAhmqM_HZ_Y979.png",
        "https://files.huizecdn.com/file1/M00/60/67/CgUA3F5PU3CAMxcbAAWk_pDnj40450.png",
        "https://files.huizecdn.com/file1/M00/60/68/CgUA3F5PVHCABYuwAARc32zYX3g345.png",
        "https://files.huizecdn.com/file1/M00/5F/42/CgUA3F5GRO2AAJWqAAK90bOyfhc547.jpg"
    ],
    "insurance_money": ""
} ]);
db.getCollection("insurance_data_fyj").insert([ {
    _id: ObjectId("5eb1756e3f273fb5c7fc6e51"),
    username: "123456",
    sex: "男",
    insurantJob: "1-6类",
    insurantDateLimit: "15年",
    paymentType: "一次性",
    insureAgeLimit: "趸交",
    premium: "10000",
    coverageAreaName: "海南省"
} ]);
db.getCollection("insurance_data_fyj").insert([ {
    _id: ObjectId("5eb3a7d20c7e74afe598270e"),
    username: "Kailin",
    sex: "男",
    insurantJob: "1-6类",
    insurantDateLimit: "10年",
    paymentType: "一次性",
    insureAgeLimit: "3年",
    premium: "1000",
    coverageAreaName: "海南省",
    "insurance_money": "1000.00"
} ]);

// ----------------------------
// Collection structure for insurance_data_tpy
// ----------------------------
db.getCollection("insurance_data_tpy").drop();
db.createCollection("insurance_data_tpy");

// ----------------------------
// Documents of insurance_data_tpy
// ----------------------------
db.getCollection("insurance_data_tpy").insert([ {
    _id: ObjectId("5eaf923318400000fe005234"),
    name: "太平财富智赢年金保险+荣耀金账户终身寿险（万能型）",
    username: 0,
    lable: [
        "快速领取",
        "固定领取",
        "万能账户"
    ],
    equity: [
        "复效:若因某些特殊原因未及时缴纳保费,导致保单停效,自停效之日起两年内,可办理相关手续使保单复效。",
        "犹豫期退保:犹豫期退保指投保人在合同约定的犹豫期内的退保。通常会扣除工本费后无息退还全部保费。",
        "退保:保险合同沒有完全履行时,经投保人和被保险人申请,保险人同意,解除双方由合同确定的法律关系,犹豫期后退保有损失,保险人按合同的约定退还保险单的现金价值。",
        "保单变更:在保单有效期内,经投保人和保险人协商同意,可以修改保单的有关内容。",
        "索赔:指当保险标的遭受承保责任范围内的风险损失或伤害时,被保险人/受益人有权向保险人提出索赔。",
        "保单贷款:指投保人将所持有的保单抵押给保险公司,按照保单现金价值的一定比例获得资金的一种借贷方式。由于质押贷款过程中客户的保险保障不受影响,所以保单依然有效。"
    ],
    notice: [
        "1.投保前请您仔细阅读：产品条款费率表客户告知书保单样本",
        "2.                                免除责任、保障责任、犹豫期、费用扣除、退保、保险单现金价值、投保人、被保险人义务等内容详见产品条款，请务必仔细阅读产品条款及电子保单的特别约定。",
        "3.本产品由太平人寿保险有限公司承保，目前该公司在北京、天津、河北、山西、内蒙古、辽宁、吉林、黑龙江、上海、江苏、浙江、安徽、福建、江西、山东、河南、湖北、湖南、广东、广西、重庆、四川、贵州、云南、陕西、甘肃、新疆、海南、青海设有分支机构。本产品的销售区域为上述区域。",
        "4.本产品承保年龄为出生满28天-65周岁（含28天、65周岁）。",
        "5.本产品支持从事1-6类职业的人士投保。",
        "6.本产品支持为本人、配偶、子女、父母投保。",
        "7.本产品投、被保险人须为中国税收居民。",
        "8.本产品不支持外籍人士投保。",
        "9.本产品最低保费为5000元，最高保费为5000000元，且为1000元的整数倍。",
        "10.您投保太平财富智赢年金保险后，在收到本合同并签收之日起可享有10日的犹豫期，当您附加太平荣耀金账户终身寿险（万能型）时享有15日的犹豫期，在犹豫期内要求解除本合同的，在保险公司收齐相关文件和资料的次日零时，本合同即被解除，保险公司自始不承担保险责任。保险公司在扣除10元工本费后，无息退还已交保险费。",
        "11.本产品提供电子保单，根据《中华人民共和国合同法》第十一条规定，数据电文是合法的合同表现形式，电子保单和纸质保单具有同等法律效力。",
        "12.本产品年交保费大于等于1万元，可搭配荣耀金万能账户，万能账户最低保费为10元。",
        "13.如果您需要附加太平荣耀金账户终身寿险（万能型），请您投保前认真阅读《太平荣耀金账户终身寿险（万能型）产品说明书》、《太平荣耀金账户终身寿险（万能型）投保提示书》、《太平荣耀金账户终身寿险（万能型）条款》。",
        "14.本产品购买生成保单后，所对应的保险责任于次日零时生效（若在生日前一日投保成功，所对应的保险责任于投保当日零时生效）。",
        "15.本太平荣耀金账户终身寿险（万能型）领取后的账户价值不应低于5000元。若万能型产品与相关年金产品同时投保，则保单相关年金产品发生犹豫期内退保终止时或犹豫期内减少保险金额后不符合保险公司的相关规定，本万能型产品终止。保单中各相关年金产品生存金、年金等各期生存权益自动转入保单下万能型产品的保单账户，且转入次数应不低于6次。以上约定，保险公司将保留调整的权利。",
        "16.太平荣耀金账户终身寿险（万能型）保险期间为终身。",
        "17.本产品相关条款名称为：太平财富智赢年金保险条款，报备文件编号为：太平寿〔2019〕384号；太平荣耀金账户终身寿险（万能型）条款，报备文件编号为：太平寿〔2019〕108号。"
    ],
    sex: [
        "男",
        "女"
    ],
    insurantJob: [
        "1-6类"
    ],
    insurantDateLimit: [
        "10"
    ],
    paymentType: [
        "年交"
    ],
    insureAgeLimit: [
        "3",
        "5"
    ],
    premium: [
        {
            value: "5000-5000000",
            min: NumberInt("5000"),
            max: NumberInt("5000000"),
            step: NumberInt("1000")
        }
    ],
    isInsure: [
        "不含",
        "含"
    ],
    "protect_interest": [
        {
            name: "生存保险金",
            fullPremium: "1万元",
            description: "自本合同第5个保险单周年日零时起至本合同期满日之前（不含本合同期满日），如果被保险人在此期间内的每个保险单周年日零时生存，保险公司按本合同的年交保险费与生存保险金给付比例的乘积给付生存保险金。生存保险金给付比例：<strong>交费期限为3年，生存保险金给付比例为60%；交费期限为5年，生存保险金给付比例为100%。</strong>"
        },
        {
            name: "满期保险金",
            fullPremium: "4070",
            description: "如果被保险人在本合同期满日零时生存，保险公司按本合同期满时的基本保险金额给付满期保险金，同时本合同终止。"
        },
        {
            name: "身故保险金",
            fullPremium: "年交保险费*被保险人身故时的保单年度数或交费年期数（取小）",
            description: "如果被保险人身故，保险公司按本合同的年交保险费与被保险人身故时本合同的保单年度数或交费年期数（以较小者为准）的乘积给付身故保险金，同时本合同终止。"
        }
    ],
    "image_url": [
        "https:http://files.huizecdn.com/file1/M00/6D/9F/CgUA3F6mpW-AIzizAAW5sfhNJwg841.png",
        "https:http://files.huizecdn.com/file1/M00/6D/9F/CgUA3F6mpXqADOIrAASVxLajWhA794.png",
        "https:http://files.huizecdn.com/file1/M00/6D/9F/CgUA3F6mpYOARARVAATuPNzYoT0604.png",
        "https:http://files.huizecdn.com/file1/M00/6D/9F/CgUA3F6mpYqAYZC_AAaO8p7oxBA214.png",
        "https:http://files.huizecdn.com/file1/M00/6C/EA/CgUA3F6igxyAK8vvAAK90bOyfhc987.jpg"
    ],
    "insurance_money": ""
} ]);
db.getCollection("insurance_data_tpy").insert([ {
    _id: ObjectId("5eb175973f273fb5c7fc6e53"),
    username: "123456",
    sex: "男",
    insurantJob: "1-6类",
    insurantDateLimit: "10",
    paymentType: "年交",
    insureAgeLimit: "3年",
    premium: NumberInt("7000"),
    isInsure: "含",
    "insurance_money": "7000.00"
} ]);
db.getCollection("insurance_data_tpy").insert([ {
    _id: ObjectId("5eb3ad81a2a142fca5900050"),
    username: "Kailin",
    sex: "男",
    insurantJob: "1-6类",
    insurantDateLimit: "10",
    paymentType: "年交",
    insureAgeLimit: "5年",
    premium: NumberInt("5000"),
    isInsure: "不含",
    "insurance_money": "5000.00"
} ]);

// ----------------------------
// Collection structure for insurance_data_zabb
// ----------------------------
db.getCollection("insurance_data_zabb").drop();
db.createCollection("insurance_data_zabb");

// ----------------------------
// Documents of insurance_data_zabb
// ----------------------------
db.getCollection("insurance_data_zabb").insert([ {
    _id: ObjectId("5eb034799fa93fa09d53a606"),
    username: 0,
    name: "珍爱宝贝教育年金保险计划",
    lable: [
        "个性化安排教育金",
        "利益稳定",
        "可选保障多"
    ],
    equity: [
        "复效:若因某些特殊原因未及时缴纳保费,导致保单停效,自停效之日起两年内,可办理相关手续使保单复效。",
        "退保:保险合同沒有完全履行时,经投保人和被保险人申请,保险人同意,解除双方由合同确定的法律关系,犹豫期后退保有损失,保险人按合同的约定退还保险单的现金价值。",
        "保单变更:在保单有效期内,经投保人和保险人协商同意,可以修改保单的有关内容。",
        "索赔:指当保险标的遭受承保责任范围内的风险损失或伤害时,被保险人/受益人有权向保险人提出索赔。"
    ],
    notice: [
        "投保前请您仔细阅读：产品条款客户告知书保单样本查看费率表",
        "责任免除、保险责任、犹豫期、费用扣除、退保、保险单现金价值、投保人、被保险人义务等内容详见产品条款，请务必仔细阅读产品条款及电子保单的特别约定。",
        "本产品由招商信诺人寿保险有限公司承保,目前该公司在北京、天津、上海、广东、浙江、福建（不含厦门）、山东、辽宁、湖北、江苏、四川、陕西、湖南、重庆、河南、江西设有分公司。本产品仅限有分公司地区的客户购买。",
        "本产品的主险承保年龄为出生满28天-13周岁(含28天、13周岁)。本产品附加险承保年龄为出生满28天-10周岁(含28天、10周岁)。",
        "本产品主险最低保额1万元。",
        "本产品投保人年龄为20-50周岁（含20、50周岁）且具有完全民事行为能力的自然人。",
        "本产品投保人须为被保险人（第一被保险人）父母；投保《招商信诺附加臻爱定期寿险》和《招商信诺附加豁免保险费重大疾病保险B款》时，被保险人（第二被保险人）为投保人本人。",
        "本产品“子女”包括继子女和养子女，“父母”包括继父母和养父母。",
        "投保前请仔细阅读本产品的相关条款、《投保须知》、《免责声明》。",
        "本产品有15天的犹豫期,在此期间,请认真审视本合同,如果认为本合同与您的需求不相符,可以在此期间提出解除本合同,保险公司将向您无息退还所交纳的保险费。若您在犹豫期后申请解除合同会有一定经济损失。",
        "本产品提供电子保单。",
        "投保人的如实告知义务，以及违反义务的后果：如果投保人故意或因重大过失未履行本产品相关条款规定的如实告知义务，足以影响保险公司决定是否同意承保或者提高保险费率的，保险公司有权解除本合同。如果投保人故意不履行如实告知义务的，保险公司对于本合同解除前发生的保险事故，保险公司不承担给付保险金的责任，并不退还保险费。如果投保人因重大过失未履行如实告知义务，对保险事故的发生有严重影响的，对于本合同解除前发生的保险事故，保险公司不承担给付保险金的责任，但应当无息退还保险费。",
        "本产品相关条款报备文件编号为：《招商信诺珍爱未来少儿教育年金保险》:招商信诺[2018]年金保险081号《招商信诺附加豁免保险费重大疾病保险》：招商信诺[2016]疾病保险013号《招商信诺附加启航高中大学教育年金保险》：招商信诺[2018]年金保险015号《招商信诺附加启航长期意外伤害医疗保险》：招商信诺[2018]医疗保险046号《招商信诺附加启航长期住院津贴医疗保险》：招商信诺[2018]医疗保险013号《招商信诺附加启航重大疾病保险》：招商信诺[2018]疾病保险014号《招商信诺附加臻爱定期寿险》：招商信诺[2017]定期寿险003号。",
        "本页面仅供参考，所述产品责任、责任免除等内容最终以《招商信诺珍爱未来少儿教育年金保险条款》，《招商信诺附加豁免保险费重大疾病保险条款》，《招商信诺附加启航高中大学教育年金保险条款》，《招商信诺附加启航长期意外伤害医疗保险条款》，《招商信诺附加启航长期住院津贴医疗保险条款》，《招商信诺附加启航重大疾病保险条款》，《招商信诺附加臻爱定期寿险条款》和正式保险合同为准。"
    ],
    policyholderExemption: [
        "不含",
        "含"
    ],
    additionalInsureAgeLimit: [
        "不投保",
        "5年",
        "10年"
    ],
    vesterSex: [
        "男",
        "女"
    ],
    sex: [
        "男",
        "女"
    ],
    province: [
        "北京市",
        "福建省",
        "广东省",
        "河南省",
        "湖北省",
        "湖南省",
        "江苏省",
        "江西省",
        "辽宁省",
        "山东省",
        "陕西省",
        "上海市",
        "四川省",
        "天津市",
        "浙江省",
        "重庆市"
    ],
    leastamount: [
        {
            value: "1-50",
            min: NumberInt("1"),
            max: NumberInt("50"),
            step: NumberInt("1")
        }
    ],
    insurantDateLimit: [
        "至25"
    ],
    insureAgeLimit: [
        "5年",
        "10年"
    ],
    paymentType: [
        "年交"
    ],
    seniorUniversityEdu: [
        {
            value: "不投保",
            min: NumberInt("0"),
            max: NumberInt("0"),
            step: NumberInt("0"),
            type: NumberInt("1"),
            unit: NumberInt("0")
        },
        {
            value: "1-50",
            min: NumberInt("1"),
            max: NumberInt("50"),
            step: NumberInt("1"),
            type: NumberInt("2"),
            unit: NumberInt("2")
        }
    ],
    seriousIllness: [
        {
            value: "不投保",
            min: NumberInt("0"),
            max: NumberInt("0"),
            step: NumberInt("0"),
            type: NumberInt("1"),
            unit: NumberInt("0")
        },
        {
            value: "1-50",
            min: NumberInt("1"),
            max: NumberInt("50"),
            step: NumberInt("1"),
            type: NumberInt("2"),
            unit: NumberInt("2")
        }
    ],
    hospitalAllowance: [
        {
            value: "不投保",
            min: NumberInt("0"),
            max: NumberInt("0"),
            step: NumberInt("0"),
            type: NumberInt("1"),
            unit: NumberInt("0")
        },
        {
            value: "50-150",
            min: NumberInt("50"),
            max: NumberInt("150"),
            step: NumberInt("50"),
            type: NumberInt("2"),
            unit: NumberInt("3")
        }
    ],
    accidentalInjury: [
        {
            value: "不投保",
            min: NumberInt("0"),
            max: NumberInt("0"),
            step: NumberInt("0"),
            type: NumberInt("1"),
            unit: NumberInt("0")
        },
        {
            value: "5000-20000",
            min: NumberInt("5000"),
            max: NumberInt("20000"),
            step: NumberInt("5000"),
            type: NumberInt("2"),
            unit: NumberInt("3")
        }
    ],
    regular: [
        {
            value: "不投保",
            min: NumberInt("0"),
            max: NumberInt("0"),
            step: NumberInt("0"),
            type: NumberInt("1"),
            unit: NumberInt("0")
        },
        {
            value: "5-30",
            min: NumberInt("5"),
            max: NumberInt("30"),
            step: NumberInt("5"),
            type: NumberInt("2"),
            unit: NumberInt("2")
        }
    ],
    additionalRiskPeriod: [
        "至21"
    ],
    "protect_interest": [
        {
            name: "身故保险金",
            description: "在保险期间内，若被保险人身故，保险公司将向受益人给付投保人累计已支付的主合同的全部保险费（不含利息），主合同及其所有附加合同的效力一并终止。"
        },
        {
            name: "教育年金",
            description: "在保险期间内，若被保险人生存至18周岁、19周岁、20周岁、21周岁、22周岁、23周岁、24周岁的保单周年日且主合同仍然有效，保险公司将在上述每一个保单周年日按主合同的基本保险金额的10%向受益人给付教育年金。"
        },
        {
            name: "（可选）身故保险金",
            description: "在保险期间内，若被保险人身故的，保险公司将按以下两项的较大者向受益人给付身故保险金：1.被保险人身故时本附加合同项下累计已支付的全部保险费；2.被保险人身故时本附加合同的现金价值。本附加合同自被保险人身故时起效力终止。"
        },
        {
            name: "（可选）高中教育年金",
            description: "在保险期间内，若被保险人在15周岁、16周岁、17周岁的保单周年日生存的，保险公司分别按本附加合同基本保险金额的100%向受益人给付高中教育年金。"
        },
        {
            name: "（可选）大学教育年金",
            description: "在保险期间内，若被保险人在18周岁、19周岁、20周岁、21周岁的保单周年日生存的，保险公司分别按本附加合同基本保险金额的100%向受益人给付大学教育年金。"
        },
        {
            name: "（可选）重大疾病保险金",
            description: "在保险期间内，若被保险人在等待期后初次发生]并经医院首次确诊患有本附加合同所规定的重大疾病，保险公司将按本附加合同的基本保险金额向受益人给付重大疾病保险金。重大疾病保险金最多给付一次。本附加合同自该重大疾病首次确诊之时起效力终止。"
        },
        {
            name: "（可选）特定重大疾病保险金",
            description: "若按照本附加合同的约定，保险公司承担给付重大疾病保险金责任的，并且该重大疾病属于本附加合同所约定的白血病、川崎病、深度昏迷、严重脑损伤或严重Ⅲ度烧伤，保险公司除给付重大疾病保险金外，另按本附加合同基本保险金额的100%向受益人给付特定重大疾病保险金。特定重大疾病保险金最多给付一次。"
        },
        {
            name: "（可选）意外住院津贴保险金",
            description: "在保险期间内，若被保险人因意外伤害导致在医院住院的，住院津贴保险金为被保险人实际住院天数乘以本附加合同基本保险金额的200%。"
        },
        {
            name: "（可选）疾病住院津贴保险金",
            description: "在保险期间内，若被保险人因保障疾病导致在医院住院的，住院津贴保险金为被保险人实际住院天数乘以本附加合同基本保险金额."
        },
        {
            name: "（可选）意外医疗保险金",
            description: "在保险期间内，若被保险人遭受意外伤害并且自该意外伤害发生之日起180天内因该意外伤害在大陆境内社会医疗保险定点医院进行治疗而在定点医院实际支出符合当地社会医疗保险支付范围的合理医疗费用（以下简称“医疗费用”）的，保险公司按以下约定向受益人给付医疗保险金：1.如该次索赔的医疗费用已从社会医疗保险、公费医疗或商业医疗保险获得补偿或赔偿，则医疗保险金=（医疗费用-医疗费用中已从社会医疗保险、公费医疗和商业医疗保险获得的补偿或赔偿）×100%；2.如该次索赔的医疗费用未从社会医疗保险、公费医疗或商业医疗保险获得补偿或赔偿，则医疗保险金=医疗费用×80%。在每一保单年度内，保险公司累计给付的医疗保险金之和以本附加合同的基本保险金额为限。保险期间届满时治疗仍未结束的，保险公司继续承担保险责任，但最长至该意外伤害发生之日起第180天。当保险公司累计给付的医疗保险金之和达到本附加合同基本保险金额的10倍时，本附加合同效力终止。"
        },
        {
            name: "（可选）身故或全残保险金",
            description: "在保险期间内，若被保险人身故或全残的，保险公司将按照本附加合同基本保险金额向受益人给付身故保险金或全残保险金。但是，如果被保险人在本附加合同的等待期内因意外伤害之外的原因导致身故或全残的，保险公司将向受益人无息退还本附加合同项下累计已支付的全部保险费。"
        },
        {
            name: "（可选）豁免保险费",
            description: "在本附加合同保险期间内，发生下列任一情形后，保险公司豁免保险单上载明的主合同及其附加合同剩余的各期保险费，本附加合同效力终止：1.本附加合同的被保险人（即主合同的投保人，下同）初次发生并经医院首次确诊患有本附加合同所规定的重大疾病；2.被保险人身故。"
        },
        {
            name: "满期保险金",
            description: "在保险期间内，若被保险人在25周岁的保单周年日仍然生存且主合同仍然有效，保险公司将按主合同的基本保险金额的50%向受益人给付满期保险金，主合同及其所有附加合同的效力一并终止。"
        }
    ],
    "image_url": [
        "https://files.huizecdn.com/file1/M00/65/12/CgUA3F5wo4CAA_RSAAhV5IgIepA884.png",
        "https://files.huizecdn.com/file1/M00/65/12/CgUA3F5wo5qAH4HGAAaNm9He8ec227.png",
        "https://files.huizecdn.com/file1/M00/65/13/CgUA3F5wo6eAa_EEAAcnB9D0fYE613.png",
        "https://files.huizecdn.com/file1/M00/65/13/CgUA3F5wo7aALloVAAsiEGKyoz8707.png",
        "https://files.huizecdn.com/file1/M00/65/13/CgUA3F5wo8CAPAIpAAK90bOyfhc083.jpg"
    ],
    "insurance_money": ""
} ]);
db.getCollection("insurance_data_zabb").insert([ {
    _id: ObjectId("5eb176a3c45ec465d9a456ae"),
    username: "123456",
    policyholderExemption: "不含",
    additionalInsureAgeLimit: "不投保",
    vesterSex: "女",
    sex: "男",
    province: "湖南省",
    leastamount: "6万元",
    insurantDateLimit: "至25岁",
    insureAgeLimit: "10年",
    paymentType: "年交",
    seniorUniversityEdu: "不投保",
    seriousIllness: "5万元",
    hospitalAllowance: "51万元",
    accidentalInjury: "15000元",
    regular: "20万元",
    additionalRiskPeriod: "至21",
    "insurance_money": "9607.10"
} ]);
db.getCollection("insurance_data_zabb").insert([ {
    _id: ObjectId("5eb3c97d76a7dda69990ca5e"),
    username: "Kailin",
    policyholderExemption: "不含",
    additionalInsureAgeLimit: "不投保",
    vesterSex: "男",
    sex: "女",
    province: "河南省",
    leastamount: "5万元",
    insurantDateLimit: "至25岁",
    insureAgeLimit: "5年",
    paymentType: "年交",
    seniorUniversityEdu: "不投保",
    seriousIllness: "15万元",
    hospitalAllowance: "100元",
    accidentalInjury: "10000元",
    regular: "25万元",
    additionalRiskPeriod: "至21",
    "insurance_money": "8986.60"
} ]);

// ----------------------------
// Collection structure for users
// ----------------------------
db.getCollection("users").drop();
db.createCollection("users");

// ----------------------------
// Documents of users
// ----------------------------
db.getCollection("users").insert([ {
    _id: ObjectId("5eaf917418400000fe005233"),
    username: "Kailin",
    password: "123456",
    mobile: "13899999999",
    "is_admin": "1"
} ]);
db.getCollection("users").insert([ {
    _id: ObjectId("5eafdd9bbeb269f7f8dc49e6"),
    username: "lailin",
    password: "123456",
    mobile: "13899999999",
    "is_admin": "0"
} ]);
db.getCollection("users").insert([ {
    _id: ObjectId("5eafdde84b1e05913abcb0ab"),
    username: "lailin",
    password: "123456",
    mobile: "13899999999",
    "is_admin": "0"
} ]);
db.getCollection("users").insert([ {
    _id: ObjectId("5eafde2023799fbbb9fc2136"),
    username: "lailin",
    password: "123456",
    mobile: "13899999999",
    "is_admin": "0"
} ]);
db.getCollection("users").insert([ {
    _id: ObjectId("5eb0edb873f180dc6db56f83"),
    username: "Kailinasd",
    password: "123456asdas",
    mobile: "135999999999",
    "is_admin": "0"
} ]);
db.getCollection("users").insert([ {
    _id: ObjectId("5eb0ede1d12c96c3f1ccbdd3"),
    username: "Kailinasd",
    password: "123456asdas",
    mobile: "13599999999",
    "is_admin": "0"
} ]);
db.getCollection("users").insert([ {
    _id: ObjectId("5eb0ededd12c96c3f1ccbdd4"),
    username: "Kailinasd",
    password: "123456asdas",
    mobile: "13588888889",
    "is_admin": "0"
} ]);
db.getCollection("users").insert([ {
    _id: ObjectId("5eb0ee0dd12c96c3f1ccbdd5"),
    username: "Kailin",
    password: "123456aa",
    mobile: "15899999999",
    "is_admin": "0"
} ]);
db.getCollection("users").insert([ {
    _id: ObjectId("5eb14a9348da52f127e09299"),
    username: "123456",
    password: "123456",
    mobile: "17899999999",
    "is_admin": "0"
} ]);
db.getCollection("users").insert([ {
    _id: ObjectId("5eb1785de253da47d23d5b5e"),
    username: "123456",
    password: "123456",
    mobile: "15999999999",
    "is_admin": "0"
} ]);
db.getCollection("users").insert([ {
    _id: ObjectId("5eb1786ae253da47d23d5b5f"),
    username: "123456aa",
    password: "123456",
    mobile: "15999999999",
    "is_admin": "0"
} ]);
db.getCollection("users").insert([ {
    _id: ObjectId("5eb178a73a39e896c806b389"),
    username: "123456aaa",
    password: "123456",
    mobile: "15999999999",
    "is_admin": "0"
} ]);
