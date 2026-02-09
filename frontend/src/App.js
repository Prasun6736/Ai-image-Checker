import { useState, useCallback } from "react";
import "@/App.css";
import axios from "axios";
import { toast } from "sonner";
import { Eye, Upload, Loader2 } from "lucide-react";

const BACKEND_URL = process.env.REACT_APP_BACKEND_URL;
const API = `${BACKEND_URL}/api`;

function App() {
  const [selectedImage, setSelectedImage] = useState(null);
  const [imagePreview, setImagePreview] = useState(null);
  const [analyzing, setAnalyzing] = useState(false);
  const [result, setResult] = useState(null);
  const [isDragging, setIsDragging] = useState(false);
  const [scanning, setScanning] = useState(false);

  const handleImageSelect = (file) => {
    if (!file) return;
    
    if (!file.type.startsWith('image/')) {
      toast.error('Please select a valid image file');
      return;
    }

    setSelectedImage(file);
    const reader = new FileReader();
    reader.onloadend = () => {
      setImagePreview(reader.result);
      setResult(null);
    };
    reader.readAsDataURL(file);
  };

  const handleDrop = useCallback((e) => {
    e.preventDefault();
    setIsDragging(false);
    
    const file = e.dataTransfer.files[0];
    handleImageSelect(file);
  }, []);

  const handleDragOver = useCallback((e) => {
    e.preventDefault();
    setIsDragging(true);
  }, []);

  const handleDragLeave = useCallback((e) => {
    e.preventDefault();
    setIsDragging(false);
  }, []);

  const analyzeImage = async () => {
    if (!selectedImage || !imagePreview) {
      toast.error('Please select an image first');
      return;
    }

    setAnalyzing(true);
    setScanning(true);
    setResult(null);

    try {
      const response = await axios.post(`${API}/analyze-image`, {
        image_base64: imagePreview
      });

      setTimeout(() => {
        setScanning(false);
        setResult(response.data);
        setAnalyzing(false);
      }, 1500);
    } catch (error) {
      console.error('Analysis error:', error);
      setAnalyzing(false);
      setScanning(false);
      toast.error(error.response?.data?.detail || 'Analysis failed. Please try again.');
    }
  };

  const reset = () => {
    setSelectedImage(null);
    setImagePreview(null);
    setResult(null);
    setScanning(false);
  };

  return (
    <div className="min-h-screen bg-white relative">
      {/* Fixed Header */}
      <header className="fixed top-0 left-0 w-full z-50 mix-blend-difference text-white p-6 md:p-12 pointer-events-none">
        <h1 className="text-2xl md:text-3xl font-display font-black tracking-tighter uppercase">VERIFY.</h1>
      </header>

      {/* Main Content */}
      <main className="max-w-2xl mx-auto px-6 md:px-12 py-24 relative z-10">
        <div className="mt-12 md:mt-24">
          {/* Title Section */}
          <div className="mb-12">
            <h2 className="text-5xl md:text-7xl font-display font-black tracking-tighter leading-none uppercase mb-4">
              IMAGE<br/>FORENSICS
            </h2>
            <p className="text-base md:text-lg font-medium leading-relaxed tracking-wide text-zinc-600 mt-6">
              Upload an image to determine its authenticity. Our AI analyzes visual patterns to detect manipulation, deepfakes, and synthetic generation.
            </p>
          </div>

          {/* Upload Zone */}
          <div
            data-testid="upload-dropzone"
            className={`relative aspect-[4/3] w-full border-2 border-dashed transition-all duration-500 ease-out flex flex-col items-center justify-center cursor-crosshair group rounded-sm overflow-hidden ${
              isDragging
                ? 'border-zinc-900 bg-zinc-50'
                : 'border-zinc-200 hover:border-zinc-900 bg-zinc-50/50 hover:bg-white'
            }`}
            onDrop={handleDrop}
            onDragOver={handleDragOver}
            onDragLeave={handleDragLeave}
            onClick={() => !imagePreview && document.getElementById('file-input').click()}
          >
            {imagePreview ? (
              <>
                <img
                  src={imagePreview}
                  alt="Selected"
                  className="w-full h-full object-cover"
                />
                {scanning && (
                  <div className="absolute inset-0 pointer-events-none">
                    <div className="scan-line absolute w-full h-[2px] bg-gradient-to-r from-transparent via-zinc-900 to-transparent"></div>
                  </div>
                )}
              </>
            ) : (
              <div className="flex flex-col items-center gap-6 p-8 text-center">
                <div className="relative">
                  <Eye className="w-16 h-16 text-zinc-300 group-hover:text-zinc-900 transition-colors duration-500" strokeWidth={1.5} />
                </div>
                <div>
                  <p className="text-xs md:text-sm font-mono text-zinc-400 uppercase tracking-widest mb-2">
                    DRAG EVIDENCE HERE
                  </p>
                  <p className="text-sm text-zinc-500 font-medium">or click to browse</p>
                </div>
              </div>
            )}
          </div>

          <input
            id="file-input"
            type="file"
            accept="image/*"
            onChange={(e) => handleImageSelect(e.target.files[0])}
            className="hidden"
          />

          {/* Action Buttons */}
          {imagePreview && (
            <div className="flex gap-4 mt-6">
              <button
                onClick={analyzeImage}
                disabled={analyzing}
                className="flex-1 bg-zinc-900 text-white font-display font-bold text-sm uppercase tracking-widest py-4 px-8 hover:bg-zinc-700 disabled:bg-zinc-400 disabled:cursor-not-allowed transition-colors duration-300 rounded-sm flex items-center justify-center gap-3"
                data-testid="analyze-button"
              >
                {analyzing ? (
                  <>
                    <Loader2 className="w-5 h-5 animate-spin" />
                    ANALYZING
                  </>
                ) : (
                  <>
                    <Upload className="w-5 h-5" />
                    ANALYZE
                  </>
                )}
              </button>
              <button
                onClick={reset}
                disabled={analyzing}
                className="bg-white border-2 border-zinc-900 text-zinc-900 font-display font-bold text-sm uppercase tracking-widest py-4 px-8 hover:bg-zinc-50 disabled:opacity-50 disabled:cursor-not-allowed transition-colors duration-300 rounded-sm"
              >
                RESET
              </button>
            </div>
          )}

          {/* Results */}
          {result && (
            <div data-testid="analysis-result" className="flex flex-col gap-4 border-t-2 border-black pt-6 mt-12">
              {/* Verdict */}
              <div className="mb-4">
                <p className="text-xs md:text-sm font-mono text-zinc-400 uppercase tracking-widest mb-3">
                  VERDICT
                </p>
                <h3
                  className={`text-[12vw] leading-none font-display font-black tracking-tighter uppercase ${
                    result.verdict === 'FAKE' ? 'text-verdict-fake' : 'text-verdict-real'
                  }`}
                >
                  {result.verdict}
                </h3>
              </div>

              {/* Confidence Score */}
              <div className="mt-6">
                <div className="flex justify-between items-center mb-3">
                  <p className="text-xs md:text-sm font-mono text-zinc-400 uppercase tracking-widest">
                    CONFIDENCE SCORE
                  </p>
                  <p
                    data-testid="confidence-score"
                    className="text-2xl font-display font-black text-zinc-900"
                  >
                    {result.confidence.toFixed(0)}%
                  </p>
                </div>
                <div className="h-2 w-full bg-zinc-100 overflow-hidden relative rounded-sm">
                  <div
                    className={`h-full transition-all duration-1000 ease-out ${
                      result.verdict === 'FAKE' ? 'bg-verdict-fake' : 'bg-verdict-real'
                    }`}
                    style={{ width: `${result.confidence}%` }}
                  ></div>
                </div>
              </div>

              {/* Details */}
              {result.details && (
                <div className="mt-6 p-6 bg-surface-subtle rounded-sm border border-zinc-200">
                  <p className="text-xs md:text-sm font-mono text-zinc-400 uppercase tracking-widest mb-3">
                    ANALYSIS DETAILS
                  </p>
                  <p className="text-sm md:text-base text-zinc-700 leading-relaxed">
                    {result.details}
                  </p>
                </div>
              )}
            </div>
          )}
        </div>
      </main>

      {/* Footer */}
      <footer className="fixed bottom-0 left-0 w-full p-6 md:p-12 pointer-events-none z-10">
        <p className="text-xs font-mono text-zinc-400 uppercase tracking-widest">
          AI-POWERED AUTHENTICITY DETECTION
        </p>
      </footer>
    </div>
  );
}

export default App;