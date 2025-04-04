import { useState } from 'react'

export default function Home() {
  const [url, setUrl] = useState('')
  const [goal, setGoal] = useState('')
  const [file, setFile] = useState(null)
  const [loading, setLoading] = useState(false)
  const [result, setResult] = useState(null)

  const handleSubmit = async () => {
    const formData = new FormData()
    formData.append('url', url)
    formData.append('brand_goal', goal)
    if (file) formData.append('file', file)

    setLoading(true)
    const res = await fetch('http://localhost:8000/audit', {
      method: 'POST',
      body: formData,
    })
    const data = await res.json()
    setResult(data)
    setLoading(false)
  }

  return (
    <main className="p-8 max-w-xl mx-auto">
      <h1 className="text-2xl font-bold mb-4">PlayMaker AI – BrandAudit</h1>
      <input type="text" placeholder="Website URL" onChange={e => setUrl(e.target.value)} className="border p-2 w-full mb-2" />
      <input type="text" placeholder="Brand Goal (optional)" onChange={e => setGoal(e.target.value)} className="border p-2 w-full mb-2" />
      <input type="file" onChange={e => setFile(e.target.files[0])} className="mb-2" />
      <button onClick={handleSubmit} className="bg-green-600 text-white px-4 py-2 rounded">Run Audit</button>
      {loading && <p>Analyzing...</p>}
      {result && (
        <div className="mt-4">
          <p><strong>Score:</strong> {result.score}/100</p>
          <p><strong>Insights:</strong> {result.insights}</p>
          <a href={result.report_url} target="_blank" className="text-blue-600 underline">Download Report</a>
        </div>
      )}
    </main>
  )
}
