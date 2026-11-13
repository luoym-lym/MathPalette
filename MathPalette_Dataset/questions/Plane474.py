"""Collected question Plane474; construction on the shared drawing protocol."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, PLANE

class Plane474:
    variants = ('C01',)

    def __init__(self):
        self.points = {
            'bar1_00': [10.0, 10.0], 'bar1_01': [11.0, 10.0], 'bar1_02': [11.0, 11.0],
            'bar1_03': [10.0, 11.0], 'bar2_00': [11.5, 9.5], 'bar2_01': [12.5, 9.5], 'bar2_02': [12.5, 10.5],
            'bar2_03': [11.5, 10.5], 'bar2_10': [11.5, 10.5], 'bar2_11': [12.5, 10.5],
            'bar2_12': [12.5, 11.5], 'bar2_13': [11.5, 11.5], 'bar3_00': [13.0, 9.0], 'bar3_01': [14.0, 9.0],
            'bar3_02': [14.0, 10.0], 'bar3_03': [13.0, 10.0], 'bar3_10': [13.0, 10.0],
            'bar3_11': [14.0, 10.0], 'bar3_12': [14.0, 11.0], 'bar3_13': [13.0, 11.0],
            'bar3_20': [13.0, 11.0], 'bar3_21': [14.0, 11.0], 'bar3_22': [14.0, 12.0],
            'bar3_23': [13.0, 12.0], 'bar4_00': [14.5, 8.5], 'bar4_01': [15.5, 8.5], 'bar4_02': [15.5, 9.5],
            'bar4_03': [14.5, 9.5], 'bar4_10': [14.5, 9.5], 'bar4_11': [15.5, 9.5], 'bar4_12': [15.5, 10.5],
            'bar4_13': [14.5, 10.5], 'bar4_20': [14.5, 10.5], 'bar4_21': [15.5, 10.5],
            'bar4_22': [15.5, 11.5], 'bar4_23': [14.5, 11.5], 'bar4_30': [14.5, 11.5],
            'bar4_31': [15.5, 11.5], 'bar4_32': [15.5, 12.5], 'bar4_33': [14.5, 12.5], 'bar5_00': [16.0, 8.0],
            'bar5_01': [17.0, 8.0], 'bar5_02': [17.0, 9.0], 'bar5_03': [16.0, 9.0], 'bar5_10': [16.0, 9.0],
            'bar5_11': [17.0, 9.0], 'bar5_12': [17.0, 10.0], 'bar5_13': [16.0, 10.0], 'bar5_20': [16.0, 10.0],
            'bar5_21': [17.0, 10.0], 'bar5_22': [17.0, 11.0], 'bar5_23': [16.0, 11.0],
            'bar5_30': [16.0, 11.0], 'bar5_31': [17.0, 11.0], 'bar5_32': [17.0, 12.0],
            'bar5_33': [16.0, 12.0], 'bar5_40': [16.0, 12.0], 'bar5_41': [17.0, 12.0],
            'bar5_42': [17.0, 13.0], 'bar5_43': [16.0, 13.0], 'board0_000': [0, 0], 'board0_001': [1, 0],
            'board0_002': [1, 1], 'board0_003': [0, 1], 'board0_010': [0, 1], 'board0_011': [1, 1],
            'board0_012': [1, 2], 'board0_013': [0, 2], 'board0_020': [0, 2], 'board0_021': [1, 2],
            'board0_022': [1, 3], 'board0_023': [0, 3], 'board0_030': [0, 3], 'board0_031': [1, 3],
            'board0_032': [1, 4], 'board0_033': [0, 4], 'board0_040': [0, 4], 'board0_041': [1, 4],
            'board0_042': [1, 5], 'board0_043': [0, 5], 'board0_100': [1, 0], 'board0_101': [2, 0],
            'board0_102': [2, 1], 'board0_103': [1, 1], 'board0_110': [1, 1], 'board0_111': [2, 1],
            'board0_112': [2, 2], 'board0_113': [1, 2], 'board0_120': [1, 2], 'board0_121': [2, 2],
            'board0_122': [2, 3], 'board0_123': [1, 3], 'board0_200': [2, 0], 'board0_201': [3, 0],
            'board0_202': [3, 1], 'board0_203': [2, 1], 'board0_210': [2, 1], 'board0_211': [3, 1],
            'board0_212': [3, 2], 'board0_213': [2, 2], 'board0_300': [3, 0], 'board0_301': [4, 0],
            'board0_302': [4, 1], 'board0_303': [3, 1], 'board0_310': [3, 1], 'board0_311': [4, 1],
            'board0_312': [4, 2], 'board0_313': [3, 2], 'board0_320': [3, 2], 'board0_321': [4, 2],
            'board0_322': [4, 3], 'board0_323': [3, 3], 'board0_330': [3, 3], 'board0_331': [4, 3],
            'board0_332': [4, 4], 'board0_333': [3, 4], 'board0_340': [3, 4], 'board0_341': [4, 4],
            'board0_342': [4, 5], 'board0_343': [3, 5], 'board1_030': [7, 3], 'board1_031': [8, 3],
            'board1_032': [8, 4], 'board1_033': [7, 4], 'board1_040': [7, 4], 'board1_041': [8, 4],
            'board1_042': [8, 5], 'board1_043': [7, 5], 'board1_120': [8, 2], 'board1_121': [9, 2],
            'board1_122': [9, 3], 'board1_123': [8, 3], 'board1_130': [8, 3], 'board1_131': [9, 3],
            'board1_132': [9, 4], 'board1_133': [8, 4], 'board1_140': [8, 4], 'board1_141': [9, 4],
            'board1_142': [9, 5], 'board1_143': [8, 5], 'board1_210': [9, 1], 'board1_211': [10, 1],
            'board1_212': [10, 2], 'board1_213': [9, 2], 'board1_220': [9, 2], 'board1_221': [10, 2],
            'board1_222': [10, 3], 'board1_223': [9, 3], 'board1_230': [9, 3], 'board1_231': [10, 3],
            'board1_232': [10, 4], 'board1_233': [9, 4], 'board1_240': [9, 4], 'board1_241': [10, 4],
            'board1_242': [10, 5], 'board1_243': [9, 5], 'board1_300': [10, 0], 'board1_301': [11, 0],
            'board1_302': [11, 1], 'board1_303': [10, 1], 'board1_310': [10, 1], 'board1_311': [11, 1],
            'board1_312': [11, 2], 'board1_313': [10, 2], 'board1_320': [10, 2], 'board1_321': [11, 2],
            'board1_322': [11, 3], 'board1_323': [10, 3], 'board1_400': [11, 0], 'board1_401': [12, 0],
            'board1_402': [12, 1], 'board1_403': [11, 1], 'board1_410': [11, 1], 'board1_411': [12, 1],
            'board1_412': [12, 2], 'board1_413': [11, 2], 'board1_420': [11, 2], 'board1_421': [12, 2],
            'board1_422': [12, 3], 'board1_423': [11, 3], 'board2_000': [14, 0], 'board2_001': [15, 0],
            'board2_002': [15, 1], 'board2_003': [14, 1], 'board2_010': [14, 1], 'board2_011': [15, 1],
            'board2_012': [15, 2], 'board2_013': [14, 2], 'board2_020': [14, 2], 'board2_021': [15, 2],
            'board2_022': [15, 3], 'board2_023': [14, 3], 'board2_030': [14, 3], 'board2_031': [15, 3],
            'board2_032': [15, 4], 'board2_033': [14, 4], 'board2_040': [14, 4], 'board2_041': [15, 4],
            'board2_042': [15, 5], 'board2_043': [14, 5], 'board2_110': [15, 1], 'board2_111': [16, 1],
            'board2_112': [16, 2], 'board2_113': [15, 2], 'board2_120': [15, 2], 'board2_121': [16, 2],
            'board2_122': [16, 3], 'board2_123': [15, 3], 'board2_130': [15, 3], 'board2_131': [16, 3],
            'board2_132': [16, 4], 'board2_133': [15, 4], 'board2_140': [15, 4], 'board2_141': [16, 4],
            'board2_142': [16, 5], 'board2_143': [15, 5], 'board2_220': [16, 2], 'board2_221': [17, 2],
            'board2_222': [17, 3], 'board2_223': [16, 3], 'board2_230': [16, 3], 'board2_231': [17, 3],
            'board2_232': [17, 4], 'board2_233': [16, 4], 'board2_240': [16, 4], 'board2_241': [17, 4],
            'board2_242': [17, 5], 'board2_243': [16, 5], 'board2_330': [17, 3], 'board2_331': [18, 3],
            'board2_332': [18, 4], 'board2_333': [17, 4], 'board2_340': [17, 4], 'board2_341': [18, 4],
            'board2_342': [18, 5], 'board2_343': [17, 5], 'board2_440': [18, 4], 'board2_441': [19, 4],
            'board2_442': [19, 5], 'board2_443': [18, 5], 'board3_000': [21, 0], 'board3_001': [22, 0],
            'board3_002': [22, 1], 'board3_003': [21, 1], 'board3_010': [21, 1], 'board3_011': [22, 1],
            'board3_012': [22, 2], 'board3_013': [21, 2], 'board3_020': [21, 2], 'board3_021': [22, 2],
            'board3_022': [22, 3], 'board3_023': [21, 3], 'board3_030': [21, 3], 'board3_031': [22, 3],
            'board3_032': [22, 4], 'board3_033': [21, 4], 'board3_040': [21, 4], 'board3_041': [22, 4],
            'board3_042': [22, 5], 'board3_043': [21, 5], 'board3_100': [22, 0], 'board3_101': [23, 0],
            'board3_102': [23, 1], 'board3_103': [22, 1], 'board3_110': [22, 1], 'board3_111': [23, 1],
            'board3_112': [23, 2], 'board3_113': [22, 2], 'board3_120': [22, 2], 'board3_121': [23, 2],
            'board3_122': [23, 3], 'board3_123': [22, 3], 'board3_130': [22, 3], 'board3_131': [23, 3],
            'board3_132': [23, 4], 'board3_133': [22, 4], 'board3_140': [22, 4], 'board3_141': [23, 4],
            'board3_142': [23, 5], 'board3_143': [22, 5], 'board3_200': [23, 0], 'board3_201': [24, 0],
            'board3_202': [24, 1], 'board3_203': [23, 1], 'board3_210': [23, 1], 'board3_211': [24, 1],
            'board3_212': [24, 2], 'board3_213': [23, 2], 'board3_220': [23, 2], 'board3_221': [24, 2],
            'board3_222': [24, 3], 'board3_223': [23, 3], 'board3_230': [23, 3], 'board3_231': [24, 3],
            'board3_232': [24, 4], 'board3_233': [23, 4], 'board3_240': [23, 4], 'board3_241': [24, 4],
            'board3_242': [24, 5], 'board3_243': [23, 5], 'board4_040': [28, 4], 'board4_041': [29, 4],
            'board4_042': [29, 5], 'board4_043': [28, 5], 'board4_110': [29, 1], 'board4_111': [30, 1],
            'board4_112': [30, 2], 'board4_113': [29, 2], 'board4_120': [29, 2], 'board4_121': [30, 2],
            'board4_122': [30, 3], 'board4_123': [29, 3], 'board4_130': [29, 3], 'board4_131': [30, 3],
            'board4_132': [30, 4], 'board4_133': [29, 4], 'board4_140': [29, 4], 'board4_141': [30, 4],
            'board4_142': [30, 5], 'board4_143': [29, 5], 'board4_200': [30, 0], 'board4_201': [31, 0],
            'board4_202': [31, 1], 'board4_203': [30, 1], 'board4_210': [30, 1], 'board4_211': [31, 1],
            'board4_212': [31, 2], 'board4_213': [30, 2], 'board4_220': [30, 2], 'board4_221': [31, 2],
            'board4_222': [31, 3], 'board4_223': [30, 3], 'board4_230': [30, 3], 'board4_231': [31, 3],
            'board4_232': [31, 4], 'board4_233': [30, 4], 'board4_240': [30, 4], 'board4_241': [31, 4],
            'board4_242': [31, 5], 'board4_243': [30, 5], 'board4_310': [31, 1], 'board4_311': [32, 1],
            'board4_312': [32, 2], 'board4_313': [31, 2], 'board4_320': [31, 2], 'board4_321': [32, 2],
            'board4_322': [32, 3], 'board4_323': [31, 3], 'board4_330': [31, 3], 'board4_331': [32, 3],
            'board4_332': [32, 4], 'board4_333': [31, 4], 'board4_340': [31, 4], 'board4_341': [32, 4],
            'board4_342': [32, 5], 'board4_343': [31, 5], 'board4_440': [32, 4], 'board4_441': [33, 4],
            'board4_442': [33, 5], 'board4_443': [32, 5]
        }

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.__class__.__name__ + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=(-0.8178507682815201, 33.872794762837614), ylim=(-10.872775022504015, 23.817870508615123)) as c:
            for object_id, vertices, codes in [('bar1_0', [self.points['bar1_00'], self.points['bar1_01'], self.points['bar1_02'], self.points['bar1_03'], self.points['bar1_00']], [1, 2, 2, 2, 79]), ('bar2_0', [self.points['bar2_00'], self.points['bar2_01'], self.points['bar2_02'], self.points['bar2_03'], self.points['bar2_00']], [1, 2, 2, 2, 79]), ('bar2_1', [self.points['bar2_10'], self.points['bar2_11'], self.points['bar2_12'], self.points['bar2_13'], self.points['bar2_10']], [1, 2, 2, 2, 79]), ('bar3_0', [self.points['bar3_00'], self.points['bar3_01'], self.points['bar3_02'], self.points['bar3_03'], self.points['bar3_00']], [1, 2, 2, 2, 79]), ('bar3_1', [self.points['bar3_10'], self.points['bar3_11'], self.points['bar3_12'], self.points['bar3_13'], self.points['bar3_10']], [1, 2, 2, 2, 79]), ('bar3_2', [self.points['bar3_20'], self.points['bar3_21'], self.points['bar3_22'], self.points['bar3_23'], self.points['bar3_20']], [1, 2, 2, 2, 79]), ('bar4_0', [self.points['bar4_00'], self.points['bar4_01'], self.points['bar4_02'], self.points['bar4_03'], self.points['bar4_00']], [1, 2, 2, 2, 79]), ('bar4_1', [self.points['bar4_10'], self.points['bar4_11'], self.points['bar4_12'], self.points['bar4_13'], self.points['bar4_10']], [1, 2, 2, 2, 79]), ('bar4_2', [self.points['bar4_20'], self.points['bar4_21'], self.points['bar4_22'], self.points['bar4_23'], self.points['bar4_20']], [1, 2, 2, 2, 79]), ('bar4_3', [self.points['bar4_30'], self.points['bar4_31'], self.points['bar4_32'], self.points['bar4_33'], self.points['bar4_30']], [1, 2, 2, 2, 79]), ('bar5_0', [self.points['bar5_00'], self.points['bar5_01'], self.points['bar5_02'], self.points['bar5_03'], self.points['bar5_00']], [1, 2, 2, 2, 79]), ('bar5_1', [self.points['bar5_10'], self.points['bar5_11'], self.points['bar5_12'], self.points['bar5_13'], self.points['bar5_10']], [1, 2, 2, 2, 79]), ('bar5_2', [self.points['bar5_20'], self.points['bar5_21'], self.points['bar5_22'], self.points['bar5_23'], self.points['bar5_20']], [1, 2, 2, 2, 79]), ('bar5_3', [self.points['bar5_30'], self.points['bar5_31'], self.points['bar5_32'], self.points['bar5_33'], self.points['bar5_30']], [1, 2, 2, 2, 79]), ('bar5_4', [self.points['bar5_40'], self.points['bar5_41'], self.points['bar5_42'], self.points['bar5_43'], self.points['bar5_40']], [1, 2, 2, 2, 79]), ('board0_00', [self.points['board0_000'], self.points['board0_001'], self.points['board0_002'], self.points['board0_003'], self.points['board0_000']], [1, 2, 2, 2, 79]), ('board0_01', [self.points['board0_010'], self.points['board0_011'], self.points['board0_012'], self.points['board0_013'], self.points['board0_010']], [1, 2, 2, 2, 79]), ('board0_02', [self.points['board0_020'], self.points['board0_021'], self.points['board0_022'], self.points['board0_023'], self.points['board0_020']], [1, 2, 2, 2, 79]), ('board0_03', [self.points['board0_030'], self.points['board0_031'], self.points['board0_032'], self.points['board0_033'], self.points['board0_030']], [1, 2, 2, 2, 79]), ('board0_04', [self.points['board0_040'], self.points['board0_041'], self.points['board0_042'], self.points['board0_043'], self.points['board0_040']], [1, 2, 2, 2, 79]), ('board0_10', [self.points['board0_100'], self.points['board0_101'], self.points['board0_102'], self.points['board0_103'], self.points['board0_100']], [1, 2, 2, 2, 79]), ('board0_11', [self.points['board0_110'], self.points['board0_111'], self.points['board0_112'], self.points['board0_113'], self.points['board0_110']], [1, 2, 2, 2, 79]), ('board0_12', [self.points['board0_120'], self.points['board0_121'], self.points['board0_122'], self.points['board0_123'], self.points['board0_120']], [1, 2, 2, 2, 79]), ('board0_20', [self.points['board0_200'], self.points['board0_201'], self.points['board0_202'], self.points['board0_203'], self.points['board0_200']], [1, 2, 2, 2, 79]), ('board0_21', [self.points['board0_210'], self.points['board0_211'], self.points['board0_212'], self.points['board0_213'], self.points['board0_210']], [1, 2, 2, 2, 79]), ('board0_30', [self.points['board0_300'], self.points['board0_301'], self.points['board0_302'], self.points['board0_303'], self.points['board0_300']], [1, 2, 2, 2, 79]), ('board0_31', [self.points['board0_310'], self.points['board0_311'], self.points['board0_312'], self.points['board0_313'], self.points['board0_310']], [1, 2, 2, 2, 79]), ('board0_32', [self.points['board0_320'], self.points['board0_321'], self.points['board0_322'], self.points['board0_323'], self.points['board0_320']], [1, 2, 2, 2, 79]), ('board0_33', [self.points['board0_330'], self.points['board0_331'], self.points['board0_332'], self.points['board0_333'], self.points['board0_330']], [1, 2, 2, 2, 79]), ('board0_34', [self.points['board0_340'], self.points['board0_341'], self.points['board0_342'], self.points['board0_343'], self.points['board0_340']], [1, 2, 2, 2, 79]), ('board1_03', [self.points['board1_030'], self.points['board1_031'], self.points['board1_032'], self.points['board1_033'], self.points['board1_030']], [1, 2, 2, 2, 79]), ('board1_04', [self.points['board1_040'], self.points['board1_041'], self.points['board1_042'], self.points['board1_043'], self.points['board1_040']], [1, 2, 2, 2, 79]), ('board1_12', [self.points['board1_120'], self.points['board1_121'], self.points['board1_122'], self.points['board1_123'], self.points['board1_120']], [1, 2, 2, 2, 79]), ('board1_13', [self.points['board1_130'], self.points['board1_131'], self.points['board1_132'], self.points['board1_133'], self.points['board1_130']], [1, 2, 2, 2, 79]), ('board1_14', [self.points['board1_140'], self.points['board1_141'], self.points['board1_142'], self.points['board1_143'], self.points['board1_140']], [1, 2, 2, 2, 79]), ('board1_21', [self.points['board1_210'], self.points['board1_211'], self.points['board1_212'], self.points['board1_213'], self.points['board1_210']], [1, 2, 2, 2, 79]), ('board1_22', [self.points['board1_220'], self.points['board1_221'], self.points['board1_222'], self.points['board1_223'], self.points['board1_220']], [1, 2, 2, 2, 79]), ('board1_23', [self.points['board1_230'], self.points['board1_231'], self.points['board1_232'], self.points['board1_233'], self.points['board1_230']], [1, 2, 2, 2, 79]), ('board1_24', [self.points['board1_240'], self.points['board1_241'], self.points['board1_242'], self.points['board1_243'], self.points['board1_240']], [1, 2, 2, 2, 79]), ('board1_30', [self.points['board1_300'], self.points['board1_301'], self.points['board1_302'], self.points['board1_303'], self.points['board1_300']], [1, 2, 2, 2, 79]), ('board1_31', [self.points['board1_310'], self.points['board1_311'], self.points['board1_312'], self.points['board1_313'], self.points['board1_310']], [1, 2, 2, 2, 79]), ('board1_32', [self.points['board1_320'], self.points['board1_321'], self.points['board1_322'], self.points['board1_323'], self.points['board1_320']], [1, 2, 2, 2, 79]), ('board1_40', [self.points['board1_400'], self.points['board1_401'], self.points['board1_402'], self.points['board1_403'], self.points['board1_400']], [1, 2, 2, 2, 79]), ('board1_41', [self.points['board1_410'], self.points['board1_411'], self.points['board1_412'], self.points['board1_413'], self.points['board1_410']], [1, 2, 2, 2, 79]), ('board1_42', [self.points['board1_420'], self.points['board1_421'], self.points['board1_422'], self.points['board1_423'], self.points['board1_420']], [1, 2, 2, 2, 79]), ('board2_00', [self.points['board2_000'], self.points['board2_001'], self.points['board2_002'], self.points['board2_003'], self.points['board2_000']], [1, 2, 2, 2, 79]), ('board2_01', [self.points['board2_010'], self.points['board2_011'], self.points['board2_012'], self.points['board2_013'], self.points['board2_010']], [1, 2, 2, 2, 79]), ('board2_02', [self.points['board2_020'], self.points['board2_021'], self.points['board2_022'], self.points['board2_023'], self.points['board2_020']], [1, 2, 2, 2, 79]), ('board2_03', [self.points['board2_030'], self.points['board2_031'], self.points['board2_032'], self.points['board2_033'], self.points['board2_030']], [1, 2, 2, 2, 79]), ('board2_04', [self.points['board2_040'], self.points['board2_041'], self.points['board2_042'], self.points['board2_043'], self.points['board2_040']], [1, 2, 2, 2, 79]), ('board2_11', [self.points['board2_110'], self.points['board2_111'], self.points['board2_112'], self.points['board2_113'], self.points['board2_110']], [1, 2, 2, 2, 79]), ('board2_12', [self.points['board2_120'], self.points['board2_121'], self.points['board2_122'], self.points['board2_123'], self.points['board2_120']], [1, 2, 2, 2, 79]), ('board2_13', [self.points['board2_130'], self.points['board2_131'], self.points['board2_132'], self.points['board2_133'], self.points['board2_130']], [1, 2, 2, 2, 79]), ('board2_14', [self.points['board2_140'], self.points['board2_141'], self.points['board2_142'], self.points['board2_143'], self.points['board2_140']], [1, 2, 2, 2, 79]), ('board2_22', [self.points['board2_220'], self.points['board2_221'], self.points['board2_222'], self.points['board2_223'], self.points['board2_220']], [1, 2, 2, 2, 79]), ('board2_23', [self.points['board2_230'], self.points['board2_231'], self.points['board2_232'], self.points['board2_233'], self.points['board2_230']], [1, 2, 2, 2, 79]), ('board2_24', [self.points['board2_240'], self.points['board2_241'], self.points['board2_242'], self.points['board2_243'], self.points['board2_240']], [1, 2, 2, 2, 79]), ('board2_33', [self.points['board2_330'], self.points['board2_331'], self.points['board2_332'], self.points['board2_333'], self.points['board2_330']], [1, 2, 2, 2, 79]), ('board2_34', [self.points['board2_340'], self.points['board2_341'], self.points['board2_342'], self.points['board2_343'], self.points['board2_340']], [1, 2, 2, 2, 79]), ('board2_44', [self.points['board2_440'], self.points['board2_441'], self.points['board2_442'], self.points['board2_443'], self.points['board2_440']], [1, 2, 2, 2, 79]), ('board3_00', [self.points['board3_000'], self.points['board3_001'], self.points['board3_002'], self.points['board3_003'], self.points['board3_000']], [1, 2, 2, 2, 79]), ('board3_01', [self.points['board3_010'], self.points['board3_011'], self.points['board3_012'], self.points['board3_013'], self.points['board3_010']], [1, 2, 2, 2, 79]), ('board3_02', [self.points['board3_020'], self.points['board3_021'], self.points['board3_022'], self.points['board3_023'], self.points['board3_020']], [1, 2, 2, 2, 79]), ('board3_03', [self.points['board3_030'], self.points['board3_031'], self.points['board3_032'], self.points['board3_033'], self.points['board3_030']], [1, 2, 2, 2, 79]), ('board3_04', [self.points['board3_040'], self.points['board3_041'], self.points['board3_042'], self.points['board3_043'], self.points['board3_040']], [1, 2, 2, 2, 79]), ('board3_10', [self.points['board3_100'], self.points['board3_101'], self.points['board3_102'], self.points['board3_103'], self.points['board3_100']], [1, 2, 2, 2, 79]), ('board3_11', [self.points['board3_110'], self.points['board3_111'], self.points['board3_112'], self.points['board3_113'], self.points['board3_110']], [1, 2, 2, 2, 79]), ('board3_12', [self.points['board3_120'], self.points['board3_121'], self.points['board3_122'], self.points['board3_123'], self.points['board3_120']], [1, 2, 2, 2, 79]), ('board3_13', [self.points['board3_130'], self.points['board3_131'], self.points['board3_132'], self.points['board3_133'], self.points['board3_130']], [1, 2, 2, 2, 79]), ('board3_14', [self.points['board3_140'], self.points['board3_141'], self.points['board3_142'], self.points['board3_143'], self.points['board3_140']], [1, 2, 2, 2, 79]), ('board3_20', [self.points['board3_200'], self.points['board3_201'], self.points['board3_202'], self.points['board3_203'], self.points['board3_200']], [1, 2, 2, 2, 79]), ('board3_21', [self.points['board3_210'], self.points['board3_211'], self.points['board3_212'], self.points['board3_213'], self.points['board3_210']], [1, 2, 2, 2, 79]), ('board3_22', [self.points['board3_220'], self.points['board3_221'], self.points['board3_222'], self.points['board3_223'], self.points['board3_220']], [1, 2, 2, 2, 79]), ('board3_23', [self.points['board3_230'], self.points['board3_231'], self.points['board3_232'], self.points['board3_233'], self.points['board3_230']], [1, 2, 2, 2, 79]), ('board3_24', [self.points['board3_240'], self.points['board3_241'], self.points['board3_242'], self.points['board3_243'], self.points['board3_240']], [1, 2, 2, 2, 79]), ('board4_04', [self.points['board4_040'], self.points['board4_041'], self.points['board4_042'], self.points['board4_043'], self.points['board4_040']], [1, 2, 2, 2, 79]), ('board4_11', [self.points['board4_110'], self.points['board4_111'], self.points['board4_112'], self.points['board4_113'], self.points['board4_110']], [1, 2, 2, 2, 79]), ('board4_12', [self.points['board4_120'], self.points['board4_121'], self.points['board4_122'], self.points['board4_123'], self.points['board4_120']], [1, 2, 2, 2, 79]), ('board4_13', [self.points['board4_130'], self.points['board4_131'], self.points['board4_132'], self.points['board4_133'], self.points['board4_130']], [1, 2, 2, 2, 79]), ('board4_14', [self.points['board4_140'], self.points['board4_141'], self.points['board4_142'], self.points['board4_143'], self.points['board4_140']], [1, 2, 2, 2, 79]), ('board4_20', [self.points['board4_200'], self.points['board4_201'], self.points['board4_202'], self.points['board4_203'], self.points['board4_200']], [1, 2, 2, 2, 79]), ('board4_21', [self.points['board4_210'], self.points['board4_211'], self.points['board4_212'], self.points['board4_213'], self.points['board4_210']], [1, 2, 2, 2, 79]), ('board4_22', [self.points['board4_220'], self.points['board4_221'], self.points['board4_222'], self.points['board4_223'], self.points['board4_220']], [1, 2, 2, 2, 79]), ('board4_23', [self.points['board4_230'], self.points['board4_231'], self.points['board4_232'], self.points['board4_233'], self.points['board4_230']], [1, 2, 2, 2, 79]), ('board4_24', [self.points['board4_240'], self.points['board4_241'], self.points['board4_242'], self.points['board4_243'], self.points['board4_240']], [1, 2, 2, 2, 79]), ('board4_31', [self.points['board4_310'], self.points['board4_311'], self.points['board4_312'], self.points['board4_313'], self.points['board4_310']], [1, 2, 2, 2, 79]), ('board4_32', [self.points['board4_320'], self.points['board4_321'], self.points['board4_322'], self.points['board4_323'], self.points['board4_320']], [1, 2, 2, 2, 79]), ('board4_33', [self.points['board4_330'], self.points['board4_331'], self.points['board4_332'], self.points['board4_333'], self.points['board4_330']], [1, 2, 2, 2, 79]), ('board4_34', [self.points['board4_340'], self.points['board4_341'], self.points['board4_342'], self.points['board4_343'], self.points['board4_340']], [1, 2, 2, 2, 79]), ('board4_44', [self.points['board4_440'], self.points['board4_441'], self.points['board4_442'], self.points['board4_443'], self.points['board4_440']], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id)
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane474_C01.png'
        _geometry_01 = [
            ('bar1_0', [[10.0, 10.0], [11.0, 10.0], [11.0, 11.0], [10.0, 11.0], [10.0, 10.0]], [1, 2, 2, 2, 79]),
            ('bar2_0', [[11.5, 9.5], [12.5, 9.5], [12.5, 10.5], [11.5, 10.5], [11.5, 9.5]], [1, 2, 2, 2, 79]),
            ('bar2_1', [[11.5, 10.5], [12.5, 10.5], [12.5, 11.5], [11.5, 11.5], [11.5, 10.5]], [1, 2, 2, 2, 79]),
            ('bar3_0', [[13.0, 9.0], [14.0, 9.0], [14.0, 10.0], [13.0, 10.0], [13.0, 9.0]], [1, 2, 2, 2, 79]),
            ('bar3_1', [[13.0, 10.0], [14.0, 10.0], [14.0, 11.0], [13.0, 11.0], [13.0, 10.0]], [1, 2, 2, 2, 79]),
            ('bar3_2', [[13.0, 11.0], [14.0, 11.0], [14.0, 12.0], [13.0, 12.0], [13.0, 11.0]], [1, 2, 2, 2, 79]),
            ('bar4_0', [[14.5, 8.5], [15.5, 8.5], [15.5, 9.5], [14.5, 9.5], [14.5, 8.5]], [1, 2, 2, 2, 79]),
            ('bar4_1', [[14.5, 9.5], [15.5, 9.5], [15.5, 10.5], [14.5, 10.5], [14.5, 9.5]], [1, 2, 2, 2, 79]),
            ('bar4_2', [[14.5, 10.5], [15.5, 10.5], [15.5, 11.5], [14.5, 11.5], [14.5, 10.5]], [1, 2, 2, 2, 79]),
            ('bar4_3', [[14.5, 11.5], [15.5, 11.5], [15.5, 12.5], [14.5, 12.5], [14.5, 11.5]], [1, 2, 2, 2, 79]),
            ('bar5_0', [[16.0, 8.0], [17.0, 8.0], [17.0, 9.0], [16.0, 9.0], [16.0, 8.0]], [1, 2, 2, 2, 79]),
            ('bar5_1', [[16.0, 9.0], [17.0, 9.0], [17.0, 10.0], [16.0, 10.0], [16.0, 9.0]], [1, 2, 2, 2, 79]),
            ('bar5_2', [[16.0, 10.0], [17.0, 10.0], [17.0, 11.0], [16.0, 11.0], [16.0, 10.0]], [1, 2, 2, 2, 79]),
            ('bar5_3', [[16.0, 11.0], [17.0, 11.0], [17.0, 12.0], [16.0, 12.0], [16.0, 11.0]], [1, 2, 2, 2, 79]),
            ('bar5_4', [[16.0, 12.0], [17.0, 12.0], [17.0, 13.0], [16.0, 13.0], [16.0, 12.0]], [1, 2, 2, 2, 79]),
            ('board0_00', [[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 1.0], [0.0, 0.0]], [1, 2, 2, 2, 79]),
            ('board0_01', [[0.0, 1.0], [1.0, 1.0], [1.0, 2.0], [0.0, 2.0], [0.0, 1.0]], [1, 2, 2, 2, 79]),
            ('board0_02', [[0.0, 2.0], [1.0, 2.0], [1.0, 3.0], [0.0, 3.0], [0.0, 2.0]], [1, 2, 2, 2, 79]),
            ('board0_03', [[0.0, 3.0], [1.0, 3.0], [1.0, 4.0], [0.0, 4.0], [0.0, 3.0]], [1, 2, 2, 2, 79]),
            ('board0_04', [[0.0, 4.0], [1.0, 4.0], [1.0, 5.0], [0.0, 5.0], [0.0, 4.0]], [1, 2, 2, 2, 79]),
            ('board0_10', [[1.0, 0.0], [2.0, 0.0], [2.0, 1.0], [1.0, 1.0], [1.0, 0.0]], [1, 2, 2, 2, 79]),
            ('board0_11', [[1.0, 1.0], [2.0, 1.0], [2.0, 2.0], [1.0, 2.0], [1.0, 1.0]], [1, 2, 2, 2, 79]),
            ('board0_12', [[1.0, 2.0], [2.0, 2.0], [2.0, 3.0], [1.0, 3.0], [1.0, 2.0]], [1, 2, 2, 2, 79]),
            ('board0_20', [[2.0, 0.0], [3.0, 0.0], [3.0, 1.0], [2.0, 1.0], [2.0, 0.0]], [1, 2, 2, 2, 79]),
            ('board0_21', [[2.0, 1.0], [3.0, 1.0], [3.0, 2.0], [2.0, 2.0], [2.0, 1.0]], [1, 2, 2, 2, 79]),
            ('board0_30', [[3.0, 0.0], [4.0, 0.0], [4.0, 1.0], [3.0, 1.0], [3.0, 0.0]], [1, 2, 2, 2, 79]),
            ('board0_31', [[3.0, 1.0], [4.0, 1.0], [4.0, 2.0], [3.0, 2.0], [3.0, 1.0]], [1, 2, 2, 2, 79]),
            ('board0_32', [[3.0, 2.0], [4.0, 2.0], [4.0, 3.0], [3.0, 3.0], [3.0, 2.0]], [1, 2, 2, 2, 79]),
            ('board0_33', [[3.0, 3.0], [4.0, 3.0], [4.0, 4.0], [3.0, 4.0], [3.0, 3.0]], [1, 2, 2, 2, 79]),
            ('board0_34', [[3.0, 4.0], [4.0, 4.0], [4.0, 5.0], [3.0, 5.0], [3.0, 4.0]], [1, 2, 2, 2, 79]),
            ('board1_03', [[7.0, 3.0], [8.0, 3.0], [8.0, 4.0], [7.0, 4.0], [7.0, 3.0]], [1, 2, 2, 2, 79]),
            ('board1_04', [[7.0, 4.0], [8.0, 4.0], [8.0, 5.0], [7.0, 5.0], [7.0, 4.0]], [1, 2, 2, 2, 79]),
            ('board1_12', [[8.0, 2.0], [9.0, 2.0], [9.0, 3.0], [8.0, 3.0], [8.0, 2.0]], [1, 2, 2, 2, 79]),
            ('board1_13', [[8.0, 3.0], [9.0, 3.0], [9.0, 4.0], [8.0, 4.0], [8.0, 3.0]], [1, 2, 2, 2, 79]),
            ('board1_14', [[8.0, 4.0], [9.0, 4.0], [9.0, 5.0], [8.0, 5.0], [8.0, 4.0]], [1, 2, 2, 2, 79]),
            ('board1_21', [[9.0, 1.0], [10.0, 1.0], [10.0, 2.0], [9.0, 2.0], [9.0, 1.0]], [1, 2, 2, 2, 79]),
            ('board1_22', [[9.0, 2.0], [10.0, 2.0], [10.0, 3.0], [9.0, 3.0], [9.0, 2.0]], [1, 2, 2, 2, 79]),
            ('board1_23', [[9.0, 3.0], [10.0, 3.0], [10.0, 4.0], [9.0, 4.0], [9.0, 3.0]], [1, 2, 2, 2, 79]),
            ('board1_24', [[9.0, 4.0], [10.0, 4.0], [10.0, 5.0], [9.0, 5.0], [9.0, 4.0]], [1, 2, 2, 2, 79]),
            ('board1_30', [[10.0, 0.0], [11.0, 0.0], [11.0, 1.0], [10.0, 1.0], [10.0, 0.0]], [1, 2, 2, 2, 79]),
            ('board1_31', [[10.0, 1.0], [11.0, 1.0], [11.0, 2.0], [10.0, 2.0], [10.0, 1.0]], [1, 2, 2, 2, 79]),
            ('board1_32', [[10.0, 2.0], [11.0, 2.0], [11.0, 3.0], [10.0, 3.0], [10.0, 2.0]], [1, 2, 2, 2, 79]),
            ('board1_40', [[11.0, 0.0], [12.0, 0.0], [12.0, 1.0], [11.0, 1.0], [11.0, 0.0]], [1, 2, 2, 2, 79]),
            ('board1_41', [[11.0, 1.0], [12.0, 1.0], [12.0, 2.0], [11.0, 2.0], [11.0, 1.0]], [1, 2, 2, 2, 79]),
            ('board1_42', [[11.0, 2.0], [12.0, 2.0], [12.0, 3.0], [11.0, 3.0], [11.0, 2.0]], [1, 2, 2, 2, 79]),
            ('board2_00', [[14.0, 0.0], [15.0, 0.0], [15.0, 1.0], [14.0, 1.0], [14.0, 0.0]], [1, 2, 2, 2, 79]),
            ('board2_01', [[14.0, 1.0], [15.0, 1.0], [15.0, 2.0], [14.0, 2.0], [14.0, 1.0]], [1, 2, 2, 2, 79]),
            ('board2_02', [[14.0, 2.0], [15.0, 2.0], [15.0, 3.0], [14.0, 3.0], [14.0, 2.0]], [1, 2, 2, 2, 79]),
            ('board2_03', [[14.0, 3.0], [15.0, 3.0], [15.0, 4.0], [14.0, 4.0], [14.0, 3.0]], [1, 2, 2, 2, 79]),
            ('board2_04', [[14.0, 4.0], [15.0, 4.0], [15.0, 5.0], [14.0, 5.0], [14.0, 4.0]], [1, 2, 2, 2, 79]),
            ('board2_11', [[15.0, 1.0], [16.0, 1.0], [16.0, 2.0], [15.0, 2.0], [15.0, 1.0]], [1, 2, 2, 2, 79]),
            ('board2_12', [[15.0, 2.0], [16.0, 2.0], [16.0, 3.0], [15.0, 3.0], [15.0, 2.0]], [1, 2, 2, 2, 79]),
            ('board2_13', [[15.0, 3.0], [16.0, 3.0], [16.0, 4.0], [15.0, 4.0], [15.0, 3.0]], [1, 2, 2, 2, 79]),
            ('board2_14', [[15.0, 4.0], [16.0, 4.0], [16.0, 5.0], [15.0, 5.0], [15.0, 4.0]], [1, 2, 2, 2, 79]),
            ('board2_22', [[16.0, 2.0], [17.0, 2.0], [17.0, 3.0], [16.0, 3.0], [16.0, 2.0]], [1, 2, 2, 2, 79]),
            ('board2_23', [[16.0, 3.0], [17.0, 3.0], [17.0, 4.0], [16.0, 4.0], [16.0, 3.0]], [1, 2, 2, 2, 79]),
            ('board2_24', [[16.0, 4.0], [17.0, 4.0], [17.0, 5.0], [16.0, 5.0], [16.0, 4.0]], [1, 2, 2, 2, 79]),
            ('board2_33', [[17.0, 3.0], [18.0, 3.0], [18.0, 4.0], [17.0, 4.0], [17.0, 3.0]], [1, 2, 2, 2, 79]),
            ('board2_34', [[17.0, 4.0], [18.0, 4.0], [18.0, 5.0], [17.0, 5.0], [17.0, 4.0]], [1, 2, 2, 2, 79]),
            ('board2_44', [[18.0, 4.0], [19.0, 4.0], [19.0, 5.0], [18.0, 5.0], [18.0, 4.0]], [1, 2, 2, 2, 79]),
            ('board3_00', [[21.0, 0.0], [22.0, 0.0], [22.0, 1.0], [21.0, 1.0], [21.0, 0.0]], [1, 2, 2, 2, 79]),
            ('board3_01', [[21.0, 1.0], [22.0, 1.0], [22.0, 2.0], [21.0, 2.0], [21.0, 1.0]], [1, 2, 2, 2, 79]),
            ('board3_02', [[21.0, 2.0], [22.0, 2.0], [22.0, 3.0], [21.0, 3.0], [21.0, 2.0]], [1, 2, 2, 2, 79]),
            ('board3_03', [[21.0, 3.0], [22.0, 3.0], [22.0, 4.0], [21.0, 4.0], [21.0, 3.0]], [1, 2, 2, 2, 79]),
            ('board3_04', [[21.0, 4.0], [22.0, 4.0], [22.0, 5.0], [21.0, 5.0], [21.0, 4.0]], [1, 2, 2, 2, 79]),
            ('board3_10', [[22.0, 0.0], [23.0, 0.0], [23.0, 1.0], [22.0, 1.0], [22.0, 0.0]], [1, 2, 2, 2, 79]),
            ('board3_11', [[22.0, 1.0], [23.0, 1.0], [23.0, 2.0], [22.0, 2.0], [22.0, 1.0]], [1, 2, 2, 2, 79]),
            ('board3_12', [[22.0, 2.0], [23.0, 2.0], [23.0, 3.0], [22.0, 3.0], [22.0, 2.0]], [1, 2, 2, 2, 79]),
            ('board3_13', [[22.0, 3.0], [23.0, 3.0], [23.0, 4.0], [22.0, 4.0], [22.0, 3.0]], [1, 2, 2, 2, 79]),
            ('board3_14', [[22.0, 4.0], [23.0, 4.0], [23.0, 5.0], [22.0, 5.0], [22.0, 4.0]], [1, 2, 2, 2, 79]),
            ('board3_20', [[23.0, 0.0], [24.0, 0.0], [24.0, 1.0], [23.0, 1.0], [23.0, 0.0]], [1, 2, 2, 2, 79]),
            ('board3_21', [[23.0, 1.0], [24.0, 1.0], [24.0, 2.0], [23.0, 2.0], [23.0, 1.0]], [1, 2, 2, 2, 79]),
            ('board3_22', [[23.0, 2.0], [24.0, 2.0], [24.0, 3.0], [23.0, 3.0], [23.0, 2.0]], [1, 2, 2, 2, 79]),
            ('board3_23', [[23.0, 3.0], [24.0, 3.0], [24.0, 4.0], [23.0, 4.0], [23.0, 3.0]], [1, 2, 2, 2, 79]),
            ('board3_24', [[23.0, 4.0], [24.0, 4.0], [24.0, 5.0], [23.0, 5.0], [23.0, 4.0]], [1, 2, 2, 2, 79]),
            ('board4_04', [[28.0, 4.0], [29.0, 4.0], [29.0, 5.0], [28.0, 5.0], [28.0, 4.0]], [1, 2, 2, 2, 79]),
            ('board4_11', [[29.0, 1.0], [30.0, 1.0], [30.0, 2.0], [29.0, 2.0], [29.0, 1.0]], [1, 2, 2, 2, 79]),
            ('board4_12', [[29.0, 2.0], [30.0, 2.0], [30.0, 3.0], [29.0, 3.0], [29.0, 2.0]], [1, 2, 2, 2, 79]),
            ('board4_13', [[29.0, 3.0], [30.0, 3.0], [30.0, 4.0], [29.0, 4.0], [29.0, 3.0]], [1, 2, 2, 2, 79]),
            ('board4_14', [[29.0, 4.0], [30.0, 4.0], [30.0, 5.0], [29.0, 5.0], [29.0, 4.0]], [1, 2, 2, 2, 79]),
            ('board4_20', [[30.0, 0.0], [31.0, 0.0], [31.0, 1.0], [30.0, 1.0], [30.0, 0.0]], [1, 2, 2, 2, 79]),
            ('board4_21', [[30.0, 1.0], [31.0, 1.0], [31.0, 2.0], [30.0, 2.0], [30.0, 1.0]], [1, 2, 2, 2, 79]),
            ('board4_22', [[30.0, 2.0], [31.0, 2.0], [31.0, 3.0], [30.0, 3.0], [30.0, 2.0]], [1, 2, 2, 2, 79]),
            ('board4_23', [[30.0, 3.0], [31.0, 3.0], [31.0, 4.0], [30.0, 4.0], [30.0, 3.0]], [1, 2, 2, 2, 79]),
            ('board4_24', [[30.0, 4.0], [31.0, 4.0], [31.0, 5.0], [30.0, 5.0], [30.0, 4.0]], [1, 2, 2, 2, 79]),
            ('board4_31', [[31.0, 1.0], [32.0, 1.0], [32.0, 2.0], [31.0, 2.0], [31.0, 1.0]], [1, 2, 2, 2, 79]),
            ('board4_32', [[31.0, 2.0], [32.0, 2.0], [32.0, 3.0], [31.0, 3.0], [31.0, 2.0]], [1, 2, 2, 2, 79]),
            ('board4_33', [[31.0, 3.0], [32.0, 3.0], [32.0, 4.0], [31.0, 4.0], [31.0, 3.0]], [1, 2, 2, 2, 79]),
            ('board4_34', [[31.0, 4.0], [32.0, 4.0], [32.0, 5.0], [31.0, 5.0], [31.0, 4.0]], [1, 2, 2, 2, 79]),
            ('board4_44', [[32.0, 4.0], [33.0, 4.0], [33.0, 5.0], [32.0, 5.0], [32.0, 4.0]], [1, 2, 2, 2, 79])
        ]
        with Canvas(PLANE, xlim=(-0.8178507682815201, 33.872794762837614), ylim=(-10.872775022504015, 23.817870508615123)) as c:
            for object_id, vertices, codes in _geometry_01:
                c.path(vertices, codes, id=object_id, capstyle='butt')
            c.line([[0.5496522111927424, 5.728569438160228], [0.5496522111927424, -1.0026628442260446]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.line([[3.5255654307740403, 5.586859284846835], [3.5609929691023887, -0.9318077675693424]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            return c.save(output_path)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane474')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01',))
    args = parser.parse_args()
    print(Plane474().draw(args.output, variant=args.variant))
