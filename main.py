import unittest

class SmartLight:
    def __init__(self, name="Living Room Light"):
        self.name = name
        self.is_on = False
        self.brightness = 50  # Default brightness percentage (0-100)
        self.color = "Warm White"  # Default color

    def turn_on(self):
        self.is_on = True
        print(f"[{self.name}] Turn on: The light is now ON.")
        return True

    def turn_off(self):
        self.is_on = False
        print(f"[{self.name}] Turn off: The light is now OFF.")
        return True

    def change_color(self, new_color):
        if self.is_on:
            self.color = new_color
            print(f"[{self.name}] Color change: Light color is now set to {self.color}.")
            return True
        else:
            print(f"[{self.name}] Cannot change color. The light is currently OFF.")
            return False

    def set_brightness(self, level):
        if 0 <= level <= 100:
            self.brightness = level
            print(f"[{self.name}] Brightness: Set to {self.brightness}%.")
            return True
        else:
            print(f"[{self.name}] Error: Brightness must be a value between 0 and 100.")
            return False


# --- Manual Object Demonstration ---
def run_manual_demo():
    print("--- Manual Object Demonstration ---")
    my_desk_light = SmartLight("Desk Light")
    
    my_desk_light.turn_on()
    my_desk_light.set_brightness(75)
    my_desk_light.change_color("Cyan")
    my_desk_light.turn_off()
    
    # Testing the safety restriction while off
    my_desk_light.change_color("Purple")
    print("-----------------------------------\n")


# --- Unit Tests ---
class TestSmartLight(unittest.TestCase):
    def setUp(self):
        self.light = SmartLight("Test Light")

    def test_initial_state(self):
        """Test that a new light starts off with correct default values."""
        self.assertFalse(self.light.is_on)
        self.assertEqual(self.light.brightness, 50)
        self.assertEqual(self.light.color, "Warm White")

    def test_turn_on_off(self):
        """Test power toggle methods."""
        self.light.turn_on()
        self.assertTrue(self.light.is_on)
        
        self.light.turn_off()
        self.assertFalse(self.light.is_on)

    def test_change_color_when_on(self):
        """Test changing color successfully when the light is powered on."""
        self.light.turn_on()
        success = self.light.change_color("Cyan")
        self.assertTrue(success)
        self.assertEqual(self.light.color, "Cyan")

    def test_change_color_when_off(self):
        """Test safety constraint: color cannot change when light is off."""
        success = self.light.change_color("Red")
        self.assertFalse(success)
        self.assertEqual(self.light.color, "Warm White")

    def test_set_brightness_valid(self):
        """Test setting brightness to a valid boundary value."""
        success = self.light.set_brightness(85)
        self.assertTrue(success)
        self.assertEqual(self.light.brightness, 85)

    def test_set_brightness_invalid(self):
        """Test boundaries for invalid brightness inputs."""
        # Above maximum (100)
        success_high = self.light.set_brightness(150)
        self.assertFalse(success_high)
        self.assertEqual(self.light.brightness, 50)

        # Below minimum (0)
        success_low = self.light.set_brightness(-10)
        self.assertFalse(success_low)
        self.assertEqual(self.light.brightness, 50)


if __name__ == "__main__":
    # 1. Run the manual test object demonstration first
    run_manual_demo()
    
    # 2. Run the automated unit tests next
    unittest.main()