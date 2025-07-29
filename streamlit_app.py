import streamlit as st



export default function VirtualTryOn() { const [uploadedImage, setUploadedImage] = useState(null); const [selectedOutfit, setSelectedOutfit] = useState(null); const previewRef = useRef(null);

const handleImageUpload = (e) => { const file = e.target.files[0]; if (file) { const reader = new FileReader(); reader.onloadend = () => { setUploadedImage(reader.result); }; reader.readAsDataURL(file); } };

const handleScreenshot = async () => { if (previewRef.current) { const canvas = await html2canvas(previewRef.current); const link = document.createElement("a"); link.download = "virtual-look.png"; link.href = canvas.toDataURL(); link.click(); } };

const outfitOptions = [ { id: 1, name: "Casual T-Shirt", url: "/outfits/tshirt1.png" }, { id: 2, name: "Kurti", url: "/outfits/kurti1.png" }, { id: 3, name: "Formal Shirt", url: "/outfits/shirt1.png" }, ];

return ( <div className="min-h-screen bg-gray-100 p-6"> <h1 className="text-3xl font-bold text-center mb-8"> Virtual Try-On Room</h1>

<div className="flex flex-col items-center gap-6">
    <input type="file" accept="image/*" onChange={handleImageUpload} className="mb-4" />

    <div className="flex gap-4">
      {outfitOptions.map((outfit) => (
        <img
          key={outfit.id}
          src={outfit.url}
          alt={outfit.name}
          className={`w-24 h-32 cursor-pointer border-2 ${
            selectedOutfit?.id === outfit.id ? "border-blue-500" : "border-transparent"
          }`}
          onClick={() => setSelectedOutfit(outfit)}
        />
      ))}
    </div>

    <div
      ref={previewRef}
      className="relative mt-6 w-[300px] h-[500px] border-2 border-dashed border-gray-400 bg-white flex items-center justify-center"
    >
      {uploadedImage && (
        <img src={uploadedImage} alt="Uploaded" className="absolute w-full h-full object-contain" />
      )}
      {selectedOutfit && (
        <img
          src={selectedOutfit.url}
          alt="Outfit"
          className="absolute w-full h-full object-contain opacity-90"
        />
      )}
    </div>

    <Button onClick={handleScreenshot} className="mt-4">
       Take Screenshot
    </Button>
  </div>
</div>

); }