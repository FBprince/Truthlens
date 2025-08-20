import { useCallback, useEffect, useMemo, useState } from 'react'

type AppState = 'input-url' | 'input-upload' | 'analyzing' | 'results'
type Verdict = 'human' | 'ai'

function App() {
  const [activeTab, setActiveTab] = useState<'url' | 'upload'>('url')
  const [state, setState] = useState<AppState>('input-url')
  const [urlValue, setUrlValue] = useState('')
  const [dragActive, setDragActive] = useState(false)
  const [statusIdx, setStatusIdx] = useState(0)
  const [confidence, setConfidence] = useState(0)
  const [verdict, setVerdict] = useState<Verdict>('ai')
  const [summary, setSummary] = useState({
    resolution: '—',
    aspectRatio: '—',
    fileType: '—',
    videoLength: ''
  })

  const statuses = useMemo(() => [
    'Analyzing pixel integrity…',
    'Scanning for artifact patterns…',
    'Cross-referencing data points…',
    'Evaluating compression noise…',
    'Comparing known model signatures…'
  ], [])

  useEffect(() => {
    if (state !== 'analyzing') return
    setStatusIdx(0)
    setConfidence(0)

    const statusTimer = setInterval(() => {
      setStatusIdx((i) => (i + 1) % statuses.length)
    }, 1800)

    const confidenceTimer = setInterval(() => {
      setConfidence((c) => Math.min(100, c + Math.ceil(Math.random() * 12)))
    }, 320)

    const doneTimer = setTimeout(() => {
      clearInterval(statusTimer)
      clearInterval(confidenceTimer)
      const isAi = Math.random() > 0.5
      setVerdict(isAi ? 'ai' : 'human')
      setConfidence(isAi ? 92 : 88)
      setSummary({
        resolution: '1920 × 1080 px',
        aspectRatio: '16:9',
        fileType: urlValue.endsWith('.mp4') ? '.mp4' : '.jpg',
        videoLength: urlValue.endsWith('.mp4') ? '01:25' : ''
      })
      setState('results')
    }, 5200)

    return () => {
      clearInterval(statusTimer)
      clearInterval(confidenceTimer)
      clearTimeout(doneTimer)
    }
  }, [state, statuses.length, urlValue])

  useEffect(() => {
    setState(activeTab === 'url' ? 'input-url' : 'input-upload')
  }, [activeTab])

  const onSubmitUrl = useCallback((e?: React.FormEvent) => {
    e?.preventDefault()
    if (!urlValue.trim()) return
    setState('analyzing')
  }, [urlValue])

  const onDrop = useCallback((e: React.DragEvent) => {
    e.preventDefault()
    e.stopPropagation()
    setDragActive(false)
    const file = e.dataTransfer.files?.[0]
    if (!file) return
    setUrlValue(file.name)
    setState('analyzing')
  }, [])

  const onBrowse = useCallback((e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0]
    if (!file) return
    setUrlValue(file.name)
    setState('analyzing')
  }, [])

  const meterFillStyle = { width: `${Math.min(confidence, 100)}%` }

  return (
    <div className="app-shell">
      <header className="header">
        <h1 className="title">Truthlens — Misinformation Scanner</h1>
        <p className="subtitle">Detect AI-generated visuals with high-confidence analysis</p>
      </header>
      <main className="main">
        <section className="panel" role="region" aria-label="Main analysis panel">
          <nav className="tabs" role="tablist" aria-label="Input method">
            <div
              role="tab"
              aria-selected={activeTab === 'url'}
              tabIndex={0}
              className={`tab ${activeTab === 'url' ? 'active' : ''}`}
              onClick={() => setActiveTab('url')}
              onKeyDown={(e) => { if (e.key === 'Enter' || e.key === ' ') setActiveTab('url') }}
            >URL</div>
            <div
              role="tab"
              aria-selected={activeTab === 'upload'}
              tabIndex={0}
              className={`tab ${activeTab === 'upload' ? 'active' : ''}`}
              onClick={() => setActiveTab('upload')}
              onKeyDown={(e) => { if (e.key === 'Enter' || e.key === ' ') setActiveTab('upload') }}
            >Media Upload</div>
          </nav>

          <div className="content">
            {state === 'input-url' && (
              <form className="url-form" onSubmit={onSubmitUrl} aria-label="URL input form">
                <input
                  className="input"
                  type="url"
                  placeholder="Paste a video or image URL address here…"
                  value={urlValue}
                  onChange={(e) => setUrlValue(e.target.value)}
                  aria-label="Media URL"
                  required
                />
                <button className="icon-button" aria-label="Scan" type="submit" title="Scan">
                  <MagnifierIcon />
                </button>
                <div className="helper">We support .jpg, .png, .mp4, .mov, .webm</div>
              </form>
            )}

            {state === 'input-upload' && (
              <div
                className={`dropzone ${dragActive ? 'drag-active' : ''}`}
                onDragEnter={(e) => { e.preventDefault(); setDragActive(true) }}
                onDragOver={(e) => { e.preventDefault(); setDragActive(true) }}
                onDragLeave={(e) => { e.preventDefault(); setDragActive(false) }}
                onDrop={onDrop}
                role="button"
                tabIndex={0}
                onKeyDown={(e) => { if (e.key === 'Enter' || e.key === ' ') (document.getElementById('file-input') as HTMLInputElement)?.click() }}
                aria-label="Drag and drop a file here or click to browse"
              >
                <div style={{ display: 'grid', placeItems: 'center' }}>
                  <FileIcon />
                  <div className="dropzone-text">Drag & Drop a file here or Click to browse</div>
                  <input id="file-input" type="file" style={{ display: 'none' }} onChange={onBrowse} />
                </div>
              </div>
            )}

            {state === 'analyzing' && (
              <div className="analysis" role="status" aria-live="polite">
                <div className="spinner" aria-hidden="true" />
                <div className="status">{statuses[statusIdx]}</div>
              </div>
            )}

            {state === 'results' && (
              <div className="results">
                <div className={`verdict ${verdict}`}>{verdict === 'ai' ? 'Likely AI-Generated' : 'Likely Human-Created'}</div>
                <div className="confidence">
                  <div className="meter" aria-label="Confidence meter" aria-valuemin={0} aria-valuemax={100} aria-valuenow={confidence} role="progressbar">
                    <div className="meter-fill" style={meterFillStyle} />
                  </div>
                  <div className="status">{confidence}% {verdict === 'ai' ? 'likely AI-Generated' : 'likely Human-Created'}</div>
                </div>
                <div className="cards">
                  <div className="card">
                    <div className="card-title">Resolution</div>
                    <div className="card-value">{summary.resolution}</div>
                  </div>
                  <div className="card">
                    <div className="card-title">Aspect Ratio</div>
                    <div className="card-value">{summary.aspectRatio}</div>
                  </div>
                  <div className="card">
                    <div className="card-title">File Type</div>
                    <div className="card-value">{summary.fileType}</div>
                  </div>
                  {summary.videoLength && (
                    <div className="card">
                      <div className="card-title">Video Length</div>
                      <div className="card-value">{summary.videoLength}</div>
                    </div>
                  )}
                </div>
                <div className="actions">
                  <button className="btn" onClick={() => setState('analyzing')}>Re-scan</button>
                  <button
                    className="btn"
                    onClick={() => navigator.clipboard.writeText(`${verdict === 'ai' ? 'Likely AI-Generated' : 'Likely Human-Created'} — ${confidence}%`)}
                  >
                    Copy report
                  </button>
                  <button className="btn primary" onClick={() => { setUrlValue(''); setActiveTab('url'); setState('input-url') }}>Start new scan</button>
                </div>
              </div>
            )}
          </div>
        </section>
      </main>
    </div>
  )
}

function MagnifierIcon() {
  return (
    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
      <path d="M11 19a8 8 0 1 0 0-16 8 8 0 0 0 0 16Z" stroke="#001018" strokeWidth="2" />
      <path d="M21 21l-4.35-4.35" stroke="#001018" strokeWidth="2" strokeLinecap="round" />
    </svg>
  )
}

function FileIcon() {
  return (
    <svg width="40" height="40" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
      <path d="M7 3h6l4 4v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2Z" stroke="var(--text-secondary)" strokeWidth="1.5" />
      <path d="M13 3v4h4" stroke="var(--text-secondary)" strokeWidth="1.5" />
    </svg>
  )
}

export default App
