import { useState } from 'react'
import { Button } from "/components/ui/button"
import { Input } from "/components/ui/input"
import { Label } from "/components/ui/label"
import { Slider } from "/components/ui/slider"
import { Textarea } from "/components/ui/textarea"
import { Play, Settings } from "lucide-react"

export default function TextToSpeechConverter() {
  const [text, setText] = useState('')
  const [rate, setRate] = useState(1)
  const [pitch, setPitch] = useState(1)

  const handleConvertToSpeech = () => {
    if ('speechSynthesis' in window) {
      const utterance = new SpeechSynthesisUtterance(text)
      utterance.rate = rate
      utterance.pitch = pitch
      window.speechSynthesis.speak(utterance)
    } else {
      alert('Speech synthesis is not supported in this browser.')
    }
  }

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-white p-4">
      <div className="max-w-2xl w-full space-y-4">
        <div className="flex items-center space-x-2">
          <Play className="w-6 h-6" />
          <h1 className="text-2xl font-bold">Text to Speech Converter</h1>
        </div>
        <Textarea
          value={text}
          onChange={(e) => setText(e.target.value)}
          placeholder="Enter text here..."
          className="resize-none"
        />
        <div className="flex flex-col space-y-2">
          <div className="flex items-center justify-between">
            <Label htmlFor="rate">Speed</Label>
            <span className="text-sm">{rate.toFixed(1)}</span>
          </div>
          <Slider
            id="rate"
            value={[rate]}
            onValueChange={(value) => setRate(value[0])}
            max={2}
            step={0.1}
            className="[&>div]:bg-blue-500"
          />
        </div>
        <div className="flex flex-col space-y-2">
          <div className="flex items-center justify-between">
            <Label htmlFor="pitch">Pitch</Label>
            <span className="text-sm">{pitch.toFixed(1)}</span>
          </div>
          <Slider
            id="pitch"
            value={[pitch]}
            onValueChange={(value) => setPitch(value[0])}
            max={2}
            step={0.1}
            className="[&>div]:bg-blue-500"
          />
        </div>
        <Button onClick={handleConvertToSpeech} className="w-full">
          Convert to Speech
        </Button>
      </div>
    </div>
  )
}
