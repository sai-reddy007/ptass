CREATE TYPE role_name AS ENUM ('SUPER_ADMIN', 'SECURITY_ADMIN', 'DEVELOPER', 'CLIENT_VIEWER');
CREATE TYPE severity AS ENUM ('critical', 'high', 'medium', 'low', 'info');
CREATE TYPE vulnerability_status AS ENUM ('open', 'triaged', 'in_progress', 'resolved', 'accepted_risk');

CREATE TABLE organizations (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL UNIQUE,
  created_at TIMESTAMP DEFAULT now()
);

CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  email VARCHAR(255) NOT NULL UNIQUE,
  full_name VARCHAR(255) NOT NULL,
  hashed_password VARCHAR(255) NOT NULL,
  role role_name NOT NULL,
  is_active BOOLEAN DEFAULT true,
  organization_id INT REFERENCES organizations(id)
);

CREATE TABLE assets (
  id SERIAL PRIMARY KEY,
  organization_id INT REFERENCES organizations(id),
  name VARCHAR(255) NOT NULL,
  asset_type VARCHAR(50) NOT NULL,
  environment VARCHAR(50) DEFAULT 'prod'
);

CREATE TABLE vulnerabilities (
  id SERIAL PRIMARY KEY,
  external_id VARCHAR(128),
  organization_id INT REFERENCES organizations(id),
  asset_id INT REFERENCES assets(id),
  severity severity NOT NULL,
  cvss VARCHAR(16),
  title VARCHAR(255) NOT NULL,
  description TEXT,
  poc TEXT,
  remediation TEXT,
  status vulnerability_status NOT NULL,
  source VARCHAR(64),
  created_at TIMESTAMP DEFAULT now(),
  updated_at TIMESTAMP DEFAULT now()
);

CREATE TABLE scans (
  id SERIAL PRIMARY KEY,
  organization_id INT REFERENCES organizations(id),
  asset_id INT REFERENCES assets(id),
  tool VARCHAR(100) NOT NULL,
  schedule_cron VARCHAR(100),
  status VARCHAR(50),
  created_at TIMESTAMP DEFAULT now()
);

CREATE TABLE reports (
  id SERIAL PRIMARY KEY,
  organization_id INT REFERENCES organizations(id),
  filename VARCHAR(255),
  file_type VARCHAR(20),
  storage_path VARCHAR(512),
  status VARCHAR(50),
  uploaded_at TIMESTAMP DEFAULT now()
);
