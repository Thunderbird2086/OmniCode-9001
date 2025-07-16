# Build Guide - GlyphMatrix

> **Note:** Even though using a pre-soldered PCB, it still requires manual soldering of hot swap sockets and LEDs.

## Parts
### Required
| Part                | Quantity | Notes                |
|---------------------|----------|----------------------|
| MX key switches     | 74       |                      |
| Hot swap sockets    | 74       |                      |
| Keycaps             | 74       |                      |
| M3x8 screws         | 6        |                      |
| Spacers (3mm)       | 6        |                      |
| M3 gaskets (0.5mm)  | 6        |                      |
| M3x4 screws         | 6        |                      |
| M3 Standoffs (5mm)  | 6        |                      |

### Optonal
| Part                | Quantity | Notes                |
|---------------------|----------|----------------------|
| RGB LEDs            | 74       | SK6812 mini-e        |
| POGO Pin 5P (curved)| 1 Set    | male and female      |
| POGO Pin 7P (curved)| 2 Set    | male and female      |

## Steps

1. **Soldering Hot Swap Sockets and LEDs**
   - **Hot Swap Sockets:** Solder all 74 hot swap sockets onto the PCB, making sure each socket is aligned with the footprint.
     ![](../img/hotswap-socket-orientation.png)
   - **Per-key LED (optional):** Solder per-key LEDs onto the PCB, making sure their orientation matches the footprint.
     ![](../img/led-footprint.png)
     ![](../img/led.png)
   - **POGO Pin (optional):**
     - Insert the POGO pins from the bottom side of the PCB, ensuring the correct orientation (male part on the left side, female part on the right for instance).
     - Hold the pins firmly in place and solder from the top side.
     - Double-check alignment before soldering all pins, as POGO pins must be straight for reliable contact.
     - After soldering, inspect for excess solder and clean up any bridges or cold joints.

1. **Install Stabilizers**
     ![](../img/stabilizers.png)

1. **Prepare Top Plate and Mounting Hardware**
   ![](../img/assemble-top-plate.png)

   - Place the top plate onto the PCB.
   - Position the 6 spacers (3mm) at the designated mounting points.
   - Add M3 gaskets (0.5mm thick) between the PCB and spacers.
   - Add 6 standoff (5mm) at the bottom side of the PCB.
   - Insert 6 M3x8mm screws through the top plate, spacers, gaskets and PCB, then loosely fasten them with 5mm standoffs.
   - **Do not fully tighten the screws yet. This is a pre-assembly step.** Final tightening should be done after all key switches are installed to ensure proper fit and alignment.

1. **Install Key Switches**
   ![](../img/keyswitch.png)
   - Carefully align each MX key switch with the hot swap socket and plate cutout.
   - Gently press the switch straight down into the socket. **Be careful:** The switch pins are easy to bend, so make sure that they are straight and enter the socket holes cleanly.
   - Double-check that each switch is fully seated and flush with the plate.
   - After installing a few switches, check that the PCB and plate remain properly aligned. Adjust if needed before continuing.
   - Once all switches are installed, you can flash the firmware and test each key to confirm proper installation and electrical contact.

1. **Secure with Screws**
   ![](../img/assemble-bottom-plate.png)
   - Place the bottom plate onto the assembled stack.
   - Use 6 M3x4mm screws for any additional mounting points as needed.
   - Tighten all screws evenly, but do not overtighten—just enough to hold everything securely and avoid damaging the PCB or plates.

1. **Add Keycaps**
   - Press the keycaps onto each switch stem. Double-check orientation and fit.

1. **Final Check**
   - Inspect all keys for proper fit and alignment.
   - Test each switch for electrical contact and smooth actuation.

## Tips
- Take your time with switch and socket installation for best results.

Enjoy your custom GlyphMatrix build!
    
## One more thing!
- If you seek to unlock the true potential of your GlyphMatrix, legends speak of two mysterious modules: [**PhaseShift**](./build_phaseshift.md) and [**DeltaForm**](./build_deltaform.md).
- When all three blocks are combined, the GlyphMatrix transcends its limits and evolves into **OmniCode:9001**, the ultimate keyboard fusion, worthy of the most legendary coders. Unleash your final form!