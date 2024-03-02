func entityParser(s string) (ans string) {
	return strings.NewReplacer(`&quot;`, `"`, `&apos;`, `'`, `&gt;`, `>`, `&lt;`, `<`, `&frasl;`, `/`, `&amp;`, `&`).Replace(s)
}