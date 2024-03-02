func categorizeBox(length, width, height, mass int) string {
    maxd := max(length, max(width, height))
    vol := length * width * height
    isBulky := maxd >= 10000 || vol >= 1e9
    isHeavy := mass >= 100
    if isBulky && isHeavy {
        return "Both"
    } else if isBulky {
        return "Bulky"
    } else if isHeavy {
        return "Heavy"
    } else {
        return "Neither"
    }
}

func max(a, b int) int {
  if a > b {
      return a
  }
  return b
}