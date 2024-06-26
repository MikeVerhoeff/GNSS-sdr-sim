library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity SPI_helper is
    generic (
        n  : integer := 4;
        clk_period : time := 1 us
    );
    port(
        word: in std_logic_vector(n-1 downto 0);
        done: out std_logic := '0';

        clk: out std_logic;
        serial_out: out std_logic
    );
end entity;

architecture behavioral of SPI_helper is
begin

    process
    begin
        clk <= '0';
        serial_out <= '0';
        loop
            wait on word;
            done <= '0';

            for i in 1 to n loop
                clk <= '0';
                serial_out <= word(n-i);
                wait for clk_period/2;
                clk <= '1';
                wait for clk_period/2;
            end loop;
            
            done <= '1';
        end loop;

    end process;

end behavioral;
