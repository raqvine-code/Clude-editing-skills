import Foundation
import Vision
import AppKit
let dir = CommandLine.arguments[1], outPath = CommandLine.arguments[2]
let files = (try! FileManager.default.contentsOfDirectory(atPath: dir)).filter{$0.hasSuffix(".jpg")}.sorted()
var lines = [String](repeating: "", count: files.count)
let lock = NSLock()
DispatchQueue.concurrentPerform(iterations: files.count) { i in
  autoreleasepool {
    guard let img = NSImage(contentsOf: URL(fileURLWithPath: dir + "/" + files[i])), let cg = img.cgImage(forProposedRect: nil, context: nil, hints: nil) else { return }
    let req = VNDetectFaceRectanglesRequest()
    try? VNImageRequestHandler(cgImage: cg, options: [:]).perform([req])
    var best: CGRect? = nil
    for o in (req.results ?? []) { if best == nil || o.boundingBox.width > best!.width { best = o.boundingBox } }
    let s = best == nil ? "\(files[i]) -" : String(format: "%@ %.4f %.4f %.4f %.4f", files[i], best!.minX, 1 - best!.maxY, best!.width, best!.height)
    lock.lock(); lines[i] = s; lock.unlock()
  }
}
try! lines.joined(separator: "\n").write(toFile: outPath, atomically: true, encoding: .utf8)
