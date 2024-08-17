# Pin Mapping for STM32 Discovery Kit (LQFP100 package)

class STM32PinMap:
    def __init__(self):
        self.pin_map = {
            'PD6': {'main_function': 'FSMC_NWAIT/ USART2 RX', 'board_function': 'PD6', 'position': 87},
            'PD7': {'main_function': 'USART2_CK/FSMC_NE1/FSMC NCE2', 'board_function': 'PD7', 'position': 88},
            'PD8': {'main_function': 'FSMC D13/ USART3 TX', 'board_function': 'PD8', 'position': 55},
            'PD9': {'main_function': 'FSMC_D14/USART3_RX', 'board_function': 'PD9', 'position': 56},
            'PD10': {'main_function': 'FSMC_D15/USART3_CK', 'board_function': 'PD10', 'position': 57},
            'PD11': {'main_function': 'FSMC_A16/USART3_CTS', 'board_function': 'PD11', 'position': 58},
            'PD12': {'main_function': 'FSMC_A17/TIM4_CH1/USART3_RTS', 'board_function': 'LED_GREEN', 'position': 59},
            'PD13': {'main_function': 'FSMC A18/ TIM4 CH2', 'board_function': 'LED_ORANGE', 'position': 60},
            'PD14': {'main_function': 'FSMC_D0/TIM4_CH3', 'board_function': 'LED_RED', 'position': 61},
            'PD15': {'main_function': 'FSMC D1/ TIM4 CH4', 'board_function': 'LED_BLUE', 'position': 62},
            'PE0': {'main_function': 'TIM4 ETR/ FSMC NBLO/ DCMI_D2', 'board_function': 'INT1', 'position': 97},
            'PE1': {'main_function': 'FSMC NBL1/ DCMI D3', 'board_function': 'INT2', 'position': 98},
            # Add other pins as needed based on your data
        }

    def get_pin_info(self, pin):
        return self.pin_map.get(pin, "Pin not found")

# Example Usage
stm32_pins = STM32PinMap()

# Get information for a specific pin, e.g., PD6
pin_info = stm32_pins.get_pin_info('PD6')
print(pin_info)

# Output:
# {'main_function': 'FSMC_NWAIT/ USART2 RX', 'board_function': 'PD6', 'position': 87}
