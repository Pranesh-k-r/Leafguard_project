# 🌿 LeafGuard AI

**LeafGuard AI** is an intelligent decision-support web application for plant health, providing deep-learning powered plant leaf disease detection, Grad-CAM explainability, lesion severity assessment, and evidence-based treatment recommendations.

---

## 🎯 Features

- **Leaf Disease Classification**: Identifies crop diseases across Pepper, Potato, and Tomato using deep convolutional neural networks.
- **Explainable AI (Grad-CAM)**: Visualizes model attention heatmaps to verify disease focus areas.
- **Disease Severity Assessment**: Calculates lesion area coverage to quantify disease progression.
- **Actionable Treatment & Care Guidance**: Offers verified organic remedies, chemical options, and preventative practices.
- **Longitudinal Recovery Tracking**: Follow-up photo logging to monitor plant healing over time.
- **Camera & Gallery Integration**: Client-side camera capture via WebRTC and file upload preview.

---

## 📁 Repository Structure

```text
LeafGuard_AI/
├── leafguard/          # Django project configuration & settings
├── accounts/           # User authentication & profile management
├── diagnosis/          # Image upload, diagnosis views & prediction flow
├── treatments/         # Agronomic treatments & plant-care catalog
├── assistant/          # Multilingual agricultural assistant
├── recovery/           # Plant recovery timeline & follow-up tracking
├── weather/            # Environmental disease risk advisory
├── ml/                 # ML pipelines, dataset inspection & evaluation scripts
├── templates/          # HTML templates
├── requirements.txt    # Python dependencies
└── manage.py           # Django management CLI
```

---

## 🚀 Getting Started

### 1. Prerequisites
- Python 3.11+
- Git

### 2. Setup Virtual Environment

```bash
# Clone the repository
git clone https://github.com/Pranesh-k-r/Leafguard_project.git
cd Leafguard_project

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Linux / macOS:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Database Migration

```bash
python manage.py migrate
```

### 4. Run Development Server

```bash
python manage.py runserver
```

Open your browser and navigate to `http://127.0.0.1:8000/`.

---

## 🔬 Datasets Used

- **PlantVillage**: 20,638 laboratory-setting images across 15 disease classes (Pepper, Potato, Tomato).
- **PlantDoc**: 2,552 in-field images used for real-world generalization evaluation.
- **PlantSeg**: 7,774 paired leaf images and semantic segmentation masks.

*(Note: Datasets are stored locally and are excluded from version control).*

---

## 🛡️ License

This project is licensed under the MIT License.
