import AVFoundation
import CoreGraphics
import ImageIO
import UniformTypeIdentifiers
import Foundation

// usage: sheet <video> <out.jpg>  -> prints "duration|WxH"
let args = CommandLine.arguments
let url = URL(fileURLWithPath: args[1])
let out = URL(fileURLWithPath: args[2])
let asset = AVURLAsset(url: url)
let dur = CMTimeGetSeconds(asset.duration)
var natW = 0.0, natH = 0.0
if let t = asset.tracks(withMediaType: .video).first {
    let s = t.naturalSize.applying(t.preferredTransform)
    natW = abs(s.width); natH = abs(s.height)
}
let gen = AVAssetImageGenerator(asset: asset)
gen.appliesPreferredTrackTransform = true
gen.maximumSize = CGSize(width: 480, height: 480)
gen.requestedTimeToleranceBefore = CMTime(seconds: 0.5, preferredTimescale: 600)
gen.requestedTimeToleranceAfter = CMTime(seconds: 0.5, preferredTimescale: 600)
var frames: [CGImage] = []
for f in [0.08, 0.35, 0.65, 0.92] {
    let t = CMTime(seconds: max(0, dur * f), preferredTimescale: 600)
    if let img = try? gen.copyCGImage(at: t, actualTime: nil) { frames.append(img) }
}
guard !frames.isEmpty else { print(String(format: "%.1f|%.0fx%.0f|NOFRAMES", dur, natW, natH)); exit(0) }
let h = 300
let widths = frames.map { Int(Double($0.width) * Double(h) / Double($0.height)) }
let gap = 6
let W = widths.reduce(0, +) + gap * (frames.count - 1)
let ctx = CGContext(data: nil, width: W, height: h, bitsPerComponent: 8, bytesPerRow: 0, space: CGColorSpaceCreateDeviceRGB(), bitmapInfo: CGImageAlphaInfo.premultipliedLast.rawValue)!
ctx.setFillColor(CGColor(red: 1, green: 0, blue: 1, alpha: 1))
ctx.fill(CGRect(x: 0, y: 0, width: W, height: h))
var x = 0
for (i, img) in frames.enumerated() {
    ctx.draw(img, in: CGRect(x: x, y: 0, width: widths[i], height: h))
    x += widths[i] + gap
}
let dest = CGImageDestinationCreateWithURL(out as CFURL, UTType.jpeg.identifier as CFString, 1, nil)!
CGImageDestinationAddImage(dest, ctx.makeImage()!, [kCGImageDestinationLossyCompressionQuality: 0.7] as CFDictionary)
CGImageDestinationFinalize(dest)
print(String(format: "%.1f|%.0fx%.0f", dur, natW, natH))
