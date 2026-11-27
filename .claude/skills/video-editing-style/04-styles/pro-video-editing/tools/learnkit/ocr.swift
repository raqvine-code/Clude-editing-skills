import Foundation
import Vision
import AppKit
// usage: ocr <dir> <out.jsonl>   OCR every .jpg in dir (sorted), one JSON line per frame
let dir = CommandLine.arguments[1], outPath = CommandLine.arguments[2]
let files = (try! FileManager.default.contentsOfDirectory(atPath: dir)).filter{$0.hasSuffix(".jpg")}.sorted()
var lines = [String](repeating: "", count: files.count)
let lock = NSLock()
DispatchQueue.concurrentPerform(iterations: files.count) { i in
  autoreleasepool {
    let url = URL(fileURLWithPath: dir + "/" + files[i])
    guard let img = NSImage(contentsOf: url), let cg = img.cgImage(forProposedRect: nil, context: nil, hints: nil) else { return }
    let req = VNRecognizeTextRequest()
    req.recognitionLevel = .accurate
    req.usesLanguageCorrection = false
    try? VNImageRequestHandler(cgImage: cg, options: [:]).perform([req])
    var obs = [[String: Any]]()
    for o in (req.results ?? []) {
      guard let c = o.topCandidates(1).first else { continue }
      let b = o.boundingBox
      obs.append(["t": c.string, "c": Double(c.confidence), "x": Double(b.minX), "y": Double(1 - b.maxY), "w": Double(b.width), "h": Double(b.height)])
    }
    let d = try! JSONSerialization.data(withJSONObject: ["f": files[i], "o": obs])
    lock.lock(); lines[i] = String(data: d, encoding: .utf8)!; lock.unlock()
  }
}
try! lines.filter{!$0.isEmpty}.joined(separator: "\n").write(toFile: outPath, atomically: true, encoding: .utf8)
