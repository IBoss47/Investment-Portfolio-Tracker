# Investment Portfolio Tracker --- 12-Week Development Roadmap

เป้าหมาย: พัฒนา Investment Portfolio Tracker สำหรับหุ้น/ETF ไทยและต่างประเทศ
บันทึกธุรกรรมด้วยตนเอง คำนวณผลตอบแทนอย่างมีหลักการ และติดตามเป้าหมายการเงิน
โดยเน้นทักษะ Data Engineering

## Tech Stack

-   Python, pandas, NumPy
-   PostgreSQL, SQL, dbt Core
-   FastAPI, Pydantic, SQLAlchemy, Alembic
-   Streamlit
-   pytest, Docker Compose, Cron, GitHub Actions
-   ทดลองใช้แหล่งข้อมูลราคา/FX เช่น `yfinance`
    โดยตรวจสอบความครอบคลุมและเงื่อนไขการใช้งาน และเตรียม CSV import
    เป็นทางเลือก

เริ่มจากการพัฒนาในเครื่องด้วยเครื่องมือฟรีก่อน ยังไม่จำเป็นต้องใช้ Cloud, Spark, Kafka,
Airflow หรือ Kubernetes ใน MVP

## Week 1 --- Requirements & Architecture

**บทบาท:** Product Analyst, Software Architect

### งาน

-   [ ] กำหนดปัญหา ผู้ใช้เป้าหมาย และขอบเขต MVP
-   [ ] นิยามเงินลงทุนสุทธิ มูลค่าพอร์ต กำไร/ขาดทุน และผลตอบแทน
-   [ ] วาด Architecture Diagram และ Data Flow
-   [ ] สร้าง Git repository, README, backlog และ `REQUIREMENTS.md`

**Deliverables:** Requirements, Architecture/Data Flow diagrams,
repository setup\
**เสร็จเมื่อ:** อธิบายเส้นทางข้อมูลตั้งแต่ต้นทางถึง dashboard ได้
และแยกเงินฝาก/ถอนออกจากกำไรอย่างชัดเจน

## Week 2 --- Database Design

**บทบาท:** Database Engineer, Data Engineer

### งาน

-   [ ] ออกแบบ ERD และ Data Dictionary
-   [ ] ออกแบบตาราง `portfolios`, `instruments`, `transactions`,
    `daily_prices`, `fx_rates`, `financial_goals`
-   [ ] กำหนด keys, constraints, indexes และชนิดข้อมูล
-   [ ] ใช้ `NUMERIC` สำหรับจำนวนเงิน/ราคาที่ต้องการความแม่นยำ
-   [ ] ตั้งค่า PostgreSQL, Alembic migrations และ seed data

**Deliverables:** ERD, Data Dictionary, schema/migrations, seed data\
**เสร็จเมื่อ:** สร้างฐานข้อมูลใหม่จาก migrations ได้ และ constraints
ช่วยป้องกันข้อมูลผิดรูปแบบ

## Week 3 --- Price & FX Ingestion

**บทบาท:** Data Engineer, Backend Engineer

### งาน

-   [ ] ทำ pipeline นำเข้าราคาสินทรัพย์และอัตราแลกเปลี่ยน
-   [ ] กำหนดรูปแบบวันที่ สกุลเงิน และรหัสสินทรัพย์
-   [ ] รองรับ CSV import เมื่อแหล่งข้อมูลอัตโนมัติใช้ไม่ได้
-   [ ] ทำ upsert เพื่อป้องกันข้อมูลซ้ำเมื่อรันซ้ำ
-   [ ] เพิ่ม logging จำนวนแถวที่อ่าน/เพิ่ม/แก้ไข/ข้าม และ error
-   [ ] ตรวจสอบ coverage และเงื่อนไขของผู้ให้บริการข้อมูล

**Deliverables:** Price pipeline, FX pipeline, CSV import, logs\
**เสร็จเมื่อ:** รันซ้ำแล้วไม่เกิดข้อมูลซ้ำ และข้อมูลราคาหรือ FX
ที่หายไปไม่ถูกแทนด้วยศูนย์โดยเงียบ ๆ

## Week 4 --- Data Quality & Transformation

**บทบาท:** Data Engineer, Analytics Engineer

### งาน

-   [ ] แบ่งชั้นข้อมูล Raw / Staging / Marts ตามความเหมาะสม
-   [ ] สร้าง dbt staging models
-   [ ] เพิ่ม tests: unique, not null, relationships, accepted values
-   [ ] ตรวจสอบข้อมูลซ้ำ วันที่ผิดปกติ สกุลเงินที่ไม่รู้จัก และธุรกรรมไม่สมบูรณ์
-   [ ] กำหนดวิธีจัดการข้อมูลหาย โดยไม่ใช้ข้อมูลอนาคตมาเติมอดีต
-   [ ] ทำเอกสาร models และ lineage ที่สำคัญ

**Deliverables:** dbt project, staging models, data quality checks\
**เสร็จเมื่อ:** tests ทำงานได้และระบบรายงานปัญหาข้อมูลอย่างชัดเจน

## Week 5 --- Transaction API

**บทบาท:** Backend Engineer, Database Engineer

### งาน

-   [ ] สร้าง FastAPI และ validation ด้วย Pydantic
-   [ ] ทำ CRUD สำหรับธุรกรรม
-   [ ] รองรับ `BUY`, `SELL`, `DIVIDEND`, `DEPOSIT`, `WITHDRAWAL`, `FEE`,
    `TAX`
-   [ ] ตรวจสอบวันที่ จำนวนหน่วย ราคา สกุลเงิน และค่าธรรมเนียม
-   [ ] ใช้ database transactions เพื่อไม่ให้บันทึกข้อมูลเพียงบางส่วน
-   [ ] เพิ่ม error responses, logging และ API tests

**Deliverables:** API endpoints, schemas, database integration, tests\
**เสร็จเมื่อ:** เพิ่ม/อ่านธุรกรรมผ่าน API ได้ และคำขอผิดรูปแบบถูกปฏิเสธอย่างชัดเจน

## Week 6 --- Portfolio Accounting

**บทบาท:** Backend Engineer, Data Engineer

### งาน

-   [ ] คำนวณจำนวนหน่วยคงเหลือจากรายการซื้อและขาย
-   [ ] คำนวณเงินสดคงเหลือแยกตามสกุลเงิน
-   [ ] คำนวณต้นทุนคงเหลือและ realized P/L
-   [ ] คำนวณมูลค่าตลาดและ unrealized P/L
-   [ ] กำหนดวิธีคิดต้นทุน MVP เช่น Weighted Average Cost
-   [ ] ระบุกติกาค่าธรรมเนียม เงินปันผล ภาษี และ corporate actions ที่รองรับ
-   [ ] แปลงมูลค่าเป็น THB ด้วยกติกา FX ที่ชัดเจน
-   [ ] สร้าง daily valuation และ reconciliation checks

**Deliverables:** Accounting module, valuation model, unit tests\
**เสร็จเมื่อ:** หน่วย เงินสด ต้นทุน และ P/L ตรงกับ test cases และแยก
realized/unrealized P/L กับเงินลงทุนสุทธิได้

## Week 7 --- Return Calculation Engine

**บทบาท:** Data Engineer, Analytics Engineer

### งาน

-   [ ] นิยามวิธีคำนวณและช่วงเวลาของแต่ละ metric
-   [ ] คำนวณ cumulative return และ annual return
-   [ ] คำนวณ XIRR จาก external cash flows ที่มีวันที่และมูลค่าพอร์ตปลายงวด
-   [ ] ใช้ CAGR เฉพาะเมื่อค่าเริ่มต้น/สิ้นสุดและช่วงเวลามีความหมายเหมาะสม
-   [ ] ทดสอบกรณีฝากหลายครั้ง ถอนเงิน และผลตอบแทนติดลบ
-   [ ] แสดงข้อจำกัดเมื่อประวัติข้อมูลไม่เพียงพอ

**Deliverables:** Return module, metrics models, unit tests\
**เสร็จเมื่อ:** ผลลัพธ์ตรงกับ expected results และไม่ใช้ `กำไร / เงินฝากสะสม`
แทนผลตอบแทนทุกกรณี

## Week 8 --- Advanced Analytics

**บทบาท:** Analytics Engineer, Data Engineer

### งาน

-   [ ] พัฒนา TWR เมื่อมี valuation ณ จุดเกิด cash flow หรือความถี่ข้อมูลเพียงพอ
-   [ ] วิเคราะห์ FX impact แยกจากการเปลี่ยนแปลงราคาตามวิธีที่กำหนด
-   [ ] สร้าง SQL/dbt marts สำหรับผลตอบแทนรายเดือนและรายปี
-   [ ] เปรียบเทียบปีก่อน ปีปัจจุบัน และค่าเฉลี่ยตั้งแต่เริ่มลงทุน โดยนิยามให้ชัด
-   [ ] ตรวจสอบความสอดคล้องระหว่างธุรกรรม มูลค่าพอร์ต และ metrics

**Deliverables:** Analytics marts, TWR (ถ้าข้อมูลรองรับ), FX analysis\
**เสร็จเมื่อ:** ทุก metric มีนิยาม ช่วงเวลา และข้อจำกัดที่ชัดเจน
และสร้างใหม่จากข้อมูลต้นทางได้

## Week 9 --- Financial Goal Planning Engine

**บทบาท:** Backend Engineer, Financial Analyst

### งาน

-   [ ] รองรับเป้าหมายเงินก้อนภายในจำนวนปีที่กำหนด
-   [ ] รองรับเป้าหมายรายได้ต่อเดือน โดยกำหนด yield หรืออัตราถอนเงิน
-   [ ] รับเงินตั้งต้น เงินลงทุนรายเดือน ระยะเวลา และผลตอบแทนสมมติ
-   [ ] คำนวณเงินลงทุนรายเดือนที่ต้องใช้หรือมูลค่าในอนาคต
-   [ ] รองรับ scenario LOW / BASE / HIGH
-   [ ] แสดงสมมติฐานเงินเฟ้อ ผลตอบแทน ค่าธรรมเนียม ภาษี และการนำรายได้กลับไปลงทุน

**Deliverables:** Goal schema/service, projection module, tests\
**เสร็จเมื่อ:** เปลี่ยนสมมติฐานแล้วผลประมาณการเปลี่ยนอย่างถูกต้อง และระบุว่าเป็น
scenario ไม่ใช่การรับประกันผลตอบแทน

## Week 10 --- Plan vs Actual & Reforecast

**บทบาท:** Data Engineer, Data Analyst

### งาน

-   [ ] เปรียบเทียบมูลค่าพอร์ตจริงกับเส้นทางเป้าหมาย
-   [ ] แสดงความคืบหน้าเป็นจำนวนเงิน เปอร์เซ็นต์ และระยะห่างจากแผน
-   [ ] ระบุสถานะเหนือ/ต่ำกว่าแผน ณ วันที่เลือก
-   [ ] ทำ reforecast เมื่อเงินลงทุนหรือผลตอบแทนจริงต่างจากสมมติฐาน
-   [ ] เก็บประวัติการคาดการณ์เพื่อเทียบย้อนหลัง
-   [ ] เตือนเมื่อข้อมูลไม่ครบหรือสมมติฐานเปลี่ยน

**Deliverables:** Plan vs Actual analytics, reforecast logic, projection
history\
**เสร็จเมื่อ:** ผู้ใช้เห็นได้ว่าตามแผนอยู่แค่ไหน และตรวจสอบการคาดการณ์ย้อนหลังได้

## Week 11 --- Dashboard & Integration

**บทบาท:** Full-stack Engineer, QA

### งาน

-   [ ] สร้าง Streamlit dashboard และเชื่อมต่อ API
-   [ ] แสดงมูลค่าพอร์ต เงินลงทุนสุทธิ และกำไร/ขาดทุน
-   [ ] แสดง annual return, cumulative return และ XIRR
-   [ ] แสดงสัดส่วนสินทรัพย์และสกุลเงิน
-   [ ] แสดง Plan vs Actual และเป้าหมายเงินก้อน/รายได้ต่อเดือน
-   [ ] จัดการ loading, error และข้อมูลไม่ครบ
-   [ ] ทดสอบ end-to-end ตั้งแต่เพิ่มธุรกรรมจนถึง dashboard

**Deliverables:** Dashboard, integrated workflow, E2E scenarios\
**เสร็จเมื่อ:** เพิ่มธุรกรรมแล้วเห็นผลในพอร์ต และ dashboard
ไม่แสดงข้อมูลหายเสมือนมีมูลค่าเป็นศูนย์

## Week 12 --- Testing, Docker & Documentation

**บทบาท:** DevOps, QA

### งาน

-   [ ] เพิ่ม unit, integration และ end-to-end tests
-   [ ] สร้าง Docker Compose สำหรับบริการที่จำเป็น
-   [ ] ตั้ง schedule pipeline ด้วย Cron ในช่วงแรก
-   [ ] ตั้ง GitHub Actions สำหรับ lint/test
-   [ ] เพิ่ม logging, error handling และแนวทาง retry
-   [ ] เขียน README วิธีติดตั้ง รัน และนำเข้าข้อมูล
-   [ ] อธิบาย architecture, ERD, data dictionary, metrics และข้อจำกัด
-   [ ] สร้าง demo dataset และทดลองเริ่มระบบจากเครื่องใหม่

**Deliverables:** Docker Compose, CI workflow, documentation, demo
walkthrough\
**เสร็จเมื่อ:** คนอื่นทำตามเอกสารเพื่อรันระบบได้ และ pipeline รันซ้ำได้พร้อม log
ที่ตรวจสอบย้อนหลังได้

## สัดส่วนเวลาแนะนำ

  ด้านงาน                                สัดส่วนโดยประมาณ
  ----------------------------------- ----------------
  Data Engineering และ Data Quality                55%
  Backend / API                                    25%
  Testing / DevOps                                 15%
  Dashboard                                         5%

ให้ความสำคัญกับความถูกต้องของข้อมูลและการคำนวณมากกว่าการตกแต่ง Dashboard

## กติกาสำคัญด้านข้อมูลและการเงิน

1.  **เงินฝากไม่ใช่กำไร:** แยก external cash flows ออกจากผลตอบแทน
2.  **เก็บประวัติ:** ต้องเก็บธุรกรรม ราคา FX และ valuation ตามวันที่
    ไม่ใช่เฉพาะยอดปัจจุบัน
3.  **รองรับหลายสกุลเงิน:** บันทึกสกุลเงินต้นทางและกติกาแปลงเป็น THB
4.  **ห้ามเดาข้อมูลที่หาย:** ไม่แทนราคา/FX ที่หายด้วยศูนย์ และไม่ใช้ข้อมูลอนาคตเติมอดีต
5.  **นิยาม Return ให้ชัด:** XIRR คำนึงถึงขนาดและเวลาของ cash flow; TWR
    ลดผลกระทบจากจังหวะฝาก/ถอนเงิน
6.  **สมมติฐานต้องมองเห็นได้:** projection ไม่ใช่การรับประกันผลตอบแทน
7.  **ตรวจสอบซ้ำได้:** metrics สำคัญต้องมี tests และตัวอย่างคำนวณด้วยมือ
8.  **ระบุข้อจำกัด MVP:** เขียนกรณี corporate actions
    และธุรกรรมซับซ้อนที่ยังไม่รองรับไว้ชัดเจน

## Definition of Done สำหรับทุกสัปดาห์

-   [ ] โค้ดอยู่ใน Git และ commit มีความหมาย
-   [ ] งานอยู่ใน scope ของ milestone ปัจจุบัน
-   [ ] มี tests ตามความเสี่ยง และรายงานผลการรันทดสอบจริง
-   [ ] มี logging/error handling ที่เหมาะสม
-   [ ] อัปเดตเอกสารที่เกี่ยวข้อง
-   [ ] บันทึกข้อจำกัด ปัญหาค้าง และงานที่เลื่อนไปสัปดาห์ถัดไป

## แนวทางใช้ AI ช่วยพัฒนา

1.  อ่าน `REQUIREMENTS.md` และเอกสารที่เกี่ยวข้องก่อนแก้โค้ด
2.  ตรวจ repository และสถานะงานปัจจุบัน
3.  สรุป requirement พร้อมเสนอไฟล์ที่จะเปลี่ยนและ acceptance criteria
4.  ทำเฉพาะ milestone ปัจจุบัน ไม่ขยาย scope เอง
5.  อธิบายก่อนเปลี่ยน schema หรือ business rules
6.  เขียนและรัน tests พร้อมรายงานผลตามจริง
7.  สรุปสิ่งที่ทำแล้ว สิ่งที่ยังไม่เสร็จ ความเสี่ยง และอัปเดตเอกสาร

## Final Acceptance Checklist

-   [ ] บันทึกธุรกรรมตามประเภทที่กำหนดได้
-   [ ] คำนวณหน่วย เงินสด ต้นทุน และ P/L ตรงกับ test cases
-   [ ] รองรับราคาและ FX หลายสกุลเงิน
-   [ ] Pipeline โหลดซ้ำได้โดยไม่สร้างข้อมูลซ้ำ
-   [ ] มี data quality checks และ logs
-   [ ] มี cumulative return, annual return และ XIRR ที่ผ่านการทดสอบ
-   [ ] มี TWR เมื่อข้อมูล valuation รองรับ
-   [ ] ตั้งเป้าหมายเงินก้อนและรายได้ต่อเดือนได้
-   [ ] เปรียบเทียบ Plan vs Actual และดูประวัติ projection ได้
-   [ ] มี unit, integration และ end-to-end tests
-   [ ] มี Docker Compose และคู่มือเริ่มต้น
-   [ ] อธิบายข้อจำกัดและสมมติฐานของข้อมูล/การคำนวณได้

------------------------------------------------------------------------

หมายเหตุ: Roadmap นี้เป็นแผน MVP 12 สัปดาห์สำหรับโปรเจกต์เดี่ยว
ควรปรับตามเวลาที่มีและความซับซ้อนของข้อมูลจริง
โดยให้ความถูกต้องของข้อมูลและการคำนวณมาก่อนจำนวนฟีเจอร์
