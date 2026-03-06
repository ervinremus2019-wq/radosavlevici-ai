# Deployment Guide

## Prerequisites
- Python 3.8+
- Node.js 16+
- Git
- Docker (optional)

## Steps

### 1. Clone the Repository
```bash
git clone https://github.com/ervinremus2019-wq/radosavlevici-ai.git
cd radosavlevici-ai
```

### 2. Install Dependencies
```bash
chmod +x scripts/install.sh
./scripts/install.sh
```

### 3. Set Up Environment
```bash
cp .env.example .env
# Edit .env as needed
```

### 4. Run the System
```bash
python3 -m core.ai_engine.main_ai
```

### 5. (Optional) Docker Deployment
```bash
docker build -t radosavlevici-ai .
docker run -p 8000:8000 radosavlevici-ai
```

## Verification
- Check logs for `System verified: Authorized user.`
- Run integrity check:
  ```bash
  python3 security/integrity_check.py
  ```

## Support
For issues, contact:
- **Primary:** ervin210@icloud.com
- **Secondary:** ervinremus2019@gmail.com