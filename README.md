# Immobilizer Assistant

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.0%2B-brightgreen)
![Supabase](https://img.shields.io/badge/Supabase-PostgreSQL-orange)

## Overview

A Python-based application for managing vehicle security system information using Supabase as the backend database. The system handles multiple manufacturers' immobilizer data, including hardware compatibility and cloning capabilities.

## Tech Stack

* Python 3.11+
* Supabase (PostgreSQL)
* Pandas for data processing
* Environment variables for configuration

## Features

- Identification of security system and key relearn procedures for various vehicle brands
- Display of download buttons for identified procedures
- Support for multiple vehicle makes and models
- VIN decode functionality to retrieve vehicle information
- Supabase storage for procedure documents
- Real-time database updates

## Database Setup

### Supabase Configuration

1. Create `.env` file:
```env
NEXT_PUBLIC_SUPABASE_URL=your_supabase_url
NEXT_PUBLIC_SUPABASE_ANON_KEY=your_supabase_key
```

2. Initialize Supabase client:
```python
from supabase import create_client
supabase = create_client(supabase_url, supabase_key)
```

### Database Schema

```sql
-- Main vehicle data table
CREATE TABLE year_make_model_table (
    id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    year INTEGER,
    make VARCHAR(50),
    model VARCHAR(100),
    security VARCHAR(50),
    parameter_reset BOOLEAN,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT TIMEZONE('utc'::TEXT, NOW()),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT TIMEZONE('utc'::TEXT, NOW())
);

-- GM brands hardware table
CREATE TABLE chevrolet_brands_hdw_table (
    id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    year INTEGER,
    make VARCHAR(50),
    model VARCHAR(100),
    security VARCHAR(50),
    hdw_pn VARCHAR(50),
    is_this_hardware_clonable BOOLEAN,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT TIMEZONE('utc'::TEXT, NOW())
);

-- Clonable modules reference table
CREATE TABLE chevrolet_clonable_table (
    id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    ecm_hardware VARCHAR(50),
    cloning_status VARCHAR(20),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT TIMEZONE('utc'::TEXT, NOW())
);
```

## VIN Decode Functionality

The application includes a VIN decode functionality to retrieve vehicle information based on the VIN. This feature uses the API `vpic.nhtsa.dot.gov/api` and is available for Toyota and Lexus only, as the security features on these makes are defined based on the trim.

## Contribution

Contributions are welcome! Feel free to open issues and pull requests for improvements and fixes.

## Contact

For more information, contact [Weverson Barbieri](https://github.com/weversonbarbieri).
