# Batch download script for Water Ways Sheet Metal images
# This script downloads all remaining images efficiently

$baseUrl = "https://waterwayssheetmetal.com"
$baseDir = "C:\Users\Brett\Dropbox\Ferret9 Global\Water Ways Sheet Metal\images"

# Bay Windows gallery (6 images)
$bayWindowsImages = @(
    "p3070143.jpg", "p7260054.jpg", "p8150037.jpg", "p8150038.jpg", "p9160061.jpg", "pc210026.jpg"
)
foreach ($img in $bayWindowsImages) {
    curl -L -o "$baseDir\our-work\bay-windows\$img" "$baseUrl/wp-content/gallery/baywindows/$img"
}

# Cupolas gallery (12 images) - need to scrape for filenames
# Finials gallery (9 images + 1 hero)
$finialsImages = @(
    "pa230008.jpg", "pb060151.jpg", "p3120163.jpg", "pa260046.jpg", "pa260065.jpg",
    "pb150123.jpg", "wsm_0611-008.jpg", "wsm_0611-026.jpg", "wsm_0611-469_cropped.jpg"
)
foreach ($img in $finialsImages) {
    curl -L -o "$baseDir\our-work\finials\$img" "$baseUrl/wp-content/gallery/finials/$img"
}

# Finials hero
curl -L -o "$baseDir\our-work\finials\pa250023.jpg" "$baseUrl/wp-content/gallery/finials/pa250023.jpg"

# Louvers gallery (9 images)
$louversImages = @(
    "pb060153.jpg", "pb060155.jpg", "p3120163.jpg", "pb060154.jpg", "p3240048.jpg",
    "386414-r1-2a-rectangle-nb-modified-249.jpg", "p1260067.jpg", "p3250056.jpg", "pa250031.jpg"
)
foreach ($img in $louversImages) {
    curl -L -o "$baseDir\our-work\louvers\$img" "$baseUrl/wp-content/gallery/louvers/$img"
}

# Roof Vents gallery (12 images)
$roofVentsImages = @(
    "p3100159.jpg", "pb060151.jpg", "p3240020.jpg", "p3250050.jpg", "p1260092.jpg",
    "p3250061.jpg", "pb030086.jpg", "p3120174.jpg", "pa260046.jpg", "p3110166.jpg",
    "p3100155.jpg", "pb030082.jpg"
)
foreach ($img in $roofVentsImages) {
    curl -L -o "$baseDir\our-work\roof-vents\$img" "$baseUrl/wp-content/gallery/roofvents/$img"
}

# Rain Chain gallery (6 images)
$rainChainImages = @(
    "pb200247.jpg", "p5120250.jpg", "p5120255.jpg", "p5040197.jpg", "p5010178.jpg", "p5010180.jpg"
)
foreach ($img in $rainChainImages) {
    curl -L -o "$baseDir\our-work\rain-chain\$img" "$baseUrl/wp-content/gallery/rain-chain/$img"
}

# Cyclone Fireplace gallery (4 images)
$cycloneImages = @(
    "p8180325.jpg", "p8180332.jpg", "p8180336.jpg", "p8180338.jpg"
)
foreach ($img in $cycloneImages) {
    curl -L -o "$baseDir\our-work\cyclone-fireplace\$img" "$baseUrl/wp-content/gallery/cyclone-fireplac/$img"
}

# Mid-Continent Tower gallery (11 images)
$midContImages = @(
    "p3060062.jpg", "p4190024.jpg", "p4190055.jpg", "p5170369.jpg", "p5180397.jpg",
    "p7070045.jpg", "p7070048.jpg", "p7080090.jpg", "p1310003.jpg", "p7050016.jpg", "p5170328.jpg"
)
foreach ($img in $midContImages) {
    curl -L -o "$baseDir\example-buildings\mid-continent-tower\$img" "$baseUrl/wp-content/gallery/mid-continent-tower/$img"
}

Write-Host "Download complete!"
