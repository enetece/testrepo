import sys

sys.path.insert(0, r"C:\Users\ContrerasN\Documents\psd_toolbox\psdtoolbox")

from psd_toolbox.pipe import Pipe
from psd_toolbox.fatigue.fatigue_tools import PipeSection

# Load data
# Min draft (md) loads
minD_path_GER_lc = r"\\dnk-czc1148lnt\f$\11959 Barossa\GLO\(308) Fat_TW_ALM - (046) + Fatigue\Results\BEND2D_12GER-2-LC_MinDraft_(25263)_(14654).xml"
minD_path_GER_uc=r"\\dnk-czc1148lnt\f$\11959 Barossa\GLO\(308) Fat_TW_ALM - (046) + Fatigue\Results\BEND2D_12GER-2-UC_MinDraft_(56354)_(19062).xml"
# Design draft (dd) loads
desD_path_GER_lc=r"\\dnk-czc1148lnt\f$\11959 Barossa\GLO\(308) Fat_TW_ALM - (046) + Fatigue\Results\BEND2D_12GER-2-LC_DesignDraft_(18655)_(76870).xml"
desD_path_GER_uc=r"\\dnk-czc1148lnt\f$\11959 Barossa\GLO\(308) Fat_TW_ALM - (046) + Fatigue\Results\BEND2D_12GER-2-UC_DesignDraft_(47289)_(19084).xml"

from psd_toolbox.global_suppl_tools.bend_xml_merger import XmlMerge

minD_load_12GER=r"\\dnk-czc1148lnt\f$\11959 Barossa\GLO\(308) Fat_TW_ALM - (046) + Fatigue\Results\BEND2D_12GER-2-LC+UC_MinDraft.xml"
XmlMerge.MergeBends(minD_path_GER_uc, minD_path_GER_lc, minD_load_12GER, offset=0)

desD_load_12GER=r"\\dnk-czc1148lnt\f$\11959 Barossa\GLO\(308) Fat_TW_ALM - (046) + Fatigue\Results\BEND2D_12GER-2-LC+UC_DesignDraft.xml"
XmlMerge.MergeBends(desD_path_GER_uc, desD_path_GER_lc, desD_load_12GER, offset=0)