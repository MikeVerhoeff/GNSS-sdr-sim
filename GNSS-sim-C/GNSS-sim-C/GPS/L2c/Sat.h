#pragma once

#include <sstream>
#include <iomanip>

#include "../../Satellite.h"
#include "Modulation.h"

namespace gps {
	namespace L2c {

		class Sat : public Satellite {
		public:
			Sat(int prn) : Satellite(prn) {
				std::stringstream ss;
				ss << "G2c" << std::setw(2) << std::setfill('0') << prn;
				name = ss.str();
			}

			virtual ChainLink* getModulation(ChainLink* dataSource) {
				Modulation* mod = new Modulation(dataSource, prn);
				return mod;
			}

			virtual int getModulationRate() {
				return 1023000;
			}

			virtual long getRadioFrequency() {
				return 122760000;
			};

			virtual int getFrameSize() {
				return 5;
			}
		};

	}
}