import os
import urllib.request
from PIL import Image

def harvest_and_transcode_suite():
    print("====================================================================")
    print("🪐 PSICO COMMUNICATIONS // HIGH-VELOCITY REPOSITORY HARVESTER")
    print("====================================================================")
    
   
    



    
    vault_path = os.path.join(os.getcwd(), "harvested_icons")
    os.makedirs(vault_path, exist_ok=True)
    target_domains = [
        # --- Tier-1 Technology, Cloud & Hardware Foundries ---
        "intel.com",
        "amd.com",
        "nvidia.com",
        "apple.com",
        "microsoft.com",
        "oracle.com",
        "ibm.com",
        "cisco.com",
        "salesforce.com",
        "atlassian.com",
        # --- Open Source, Developer Languages & Frameworks ---
        "python.org",
        "nodejs.org",
        "rust-lang.org",
        "golang.org",
        "php.net",
        "ruby-lang.org",
        "typescriptlang.org",
        "npmjs.com",
        "nuget.org",
        "rubygems.org",
        "packagist.org",
        "crates.io",
        "maven.org",
        "apache.org",
        "gnu.org",
        # --- Advanced Electronics, Hardware & Component Sourcing ---
        "rs-online.com",
        "farnell.com",
        "mouser.co.uk",
        "digikey.co.uk",
        "adafruit.com",
        "sparkfun.com",
        "pcbway.com",
        "jlcpcb.com",
        "ifixit.com",
        "raspberrypi.com",
        # --- Alternative Creator Platforms, Art & Documentation ---
        "artstation.com",
        "deviantart.com",
        "behance.net",
        "dribbble.com",
        "pixiv.net",
        "flickr.com",
        "unsplash.com",
        "pixabay.com",
        "pexels.com",
        "vimeo.com",
        # --- Independent Research, Science & Space Telemetry ---
        "nasa.gov",
        "esa.int",
        "cern.ch",
        "arxiv.org",
        "nature.com",
        "science.org",
        "ncbi.nlm.nih.gov",
        "sciencedirect.com",
        "ieee.org",
        "space.com",
        # --- Global Logistics, Transit & Aviation Frameworks ---
        "flightradar24.com",
        "marinetraffic.com",
        "royalmail.com",
        "dhl.com",
        "fedex.com",
        "ups.com",
        "nationalrail.co.uk",
        "tfl.gov.uk",
        "flightaware.com",
        "skyscanner.net",
        # --- Premium Education, Documentation & Open Courseware ---
        "coursera.org",
        "edx.org",
        "udemy.com",
        "khanacademy.org",
        "duolingo.com",
        "codecademy.com",
        "mit.edu",
        "stanford.edu",
        "harvard.edu",
        "ox.ac.uk",
        # --- Deep Reference Registers, Patents & Specialized Logs ---
        "epo.org",
        "uspto.gov",
        "wipo.int",
        "imdb.com",
        "goodreads.com",
        "discogs.com",
        "allmusic.com",
        "letterboxd.com",
        "boardgamegeek.com",
        "kickstarter.com",
        # --- Global Consumer Services, Utilities & Housing Maps ---
        "zoopla.co.uk",
        "rightmove.co.uk",
        "autotrader.co.uk",
        "booking.com",
        "airbnb.co.uk",
        "tripadvisor.co.uk",
        "uber.com",
        "deliveroo.co.uk",
        "justeat.co.uk",
        "paypal.com"
    ]









    print(f"📡 Vault Ground Established: \\harvested_icons\\\n")
    
    for domain in target_domains:
        print(f"🏹 Sweeping target node wire: [{domain}] ...")
        
        safe_name = domain.replace(".", "_")
        temp_png = os.path.join(vault_path, f"temp_{safe_name}.png")
        final_ico = os.path.join(vault_path, f"{safe_name}.ico")
        
        # Pure loop variable assignment string matrix
        gstatic_url = f"https://www.google.com/s2/favicons?domain={domain}&size=128"
        try:
            req = urllib.request.Request(
                gstatic_url, 
                headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:132.0) Gecko/20100101 Firefox/132.0'}
            )
            
            with urllib.request.urlopen(req, timeout=10) as response:
                with open(temp_png, "wb") as f:
                    f.write(response.read())
            
            img = Image.open(temp_png)
            icon_sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128)]
            img.save(final_ico, format="ICO", sizes=icon_sizes)
            print(f"   └── 🗜️  SUCCESS: Transcoded and stored -> {os.path.basename(final_ico)}")
            
        except Exception as e:
            print(f"   └── ❌ DROP EXCEPTION: Unable to fetch node off gstatic wire. Details: {e}")
            
        if os.path.exists(temp_png):
            os.remove(temp_png)
            
    print("\n🪐 HARVEST MATRIX Finalized: Your custom asset library is baked flat to disk.")
    print("====================================================================")

if __name__ == "__main__":
    harvest_and_transcode_suite()


