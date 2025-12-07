import { motion } from "framer-motion"
import { PROFILE } from "@/data/profile"
import { Badge } from "@/components/ui/badge"
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs"
import { Card, CardContent, CardHeader, CardTitle, CardDescription } from "@/components/ui/card"

export const Skills = () => {
    const categories = [
        { id: "languages", label: "Languages", items: PROFILE.skills.languages },
        { id: "frameworks", label: "Frameworks", items: PROFILE.skills.frameworks },
        { id: "tools", label: "Tools", items: PROFILE.skills.tools },
        { id: "concepts", label: "Concepts", items: PROFILE.skills.concepts },
    ]

    return (
        <section id="skills" className="py-20 scroll-mt-16 bg-muted/30">
            <div className="container">
                <motion.div
                    initial={{ opacity: 0, y: 20 }}
                    whileInView={{ opacity: 1, y: 0 }}
                    viewport={{ once: true }}
                    transition={{ duration: 0.5 }}
                    className="space-y-8"
                >
                    <div className="space-y-2">
                        <h2 className="text-3xl font-bold tracking-tight">Technical Skills</h2>
                        <p className="text-muted-foreground">My technical toolkit for building robust automation solutions.</p>
                    </div>

                    <Tabs defaultValue="languages" className="w-full">
                        <TabsList className="grid w-full grid-cols-2 lg:grid-cols-4 mb-8">
                            {categories.map((cat) => (
                                <TabsTrigger key={cat.id} value={cat.id}>
                                    {cat.label}
                                </TabsTrigger>
                            ))}
                        </TabsList>

                        {categories.map((cat) => (
                            <TabsContent key={cat.id} value={cat.id} className="mt-0">
                                <Card>
                                    <CardHeader>
                                        <CardTitle>{cat.label}</CardTitle>
                                        <CardDescription>
                                            Core competencies in {cat.label.toLowerCase()}.
                                        </CardDescription>
                                    </CardHeader>
                                    <CardContent className="flex flex-wrap gap-2">
                                        {cat.items.map((skill) => (
                                            <Badge key={skill} variant="secondary" className="text-md py-1 px-3">
                                                {skill}
                                            </Badge>
                                        ))}
                                    </CardContent>
                                </Card>
                            </TabsContent>
                        ))}
                    </Tabs>
                </motion.div>
            </div>
        </section>
    )
}
